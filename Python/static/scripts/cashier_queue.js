document.addEventListener("DOMContentLoaded", (event) => {
   async function fetchQueue() {
      try {
         const response = await fetch("/api/queue");
         const data = await response.json();

         // Clear the queue container
         const queueContainer = document.getElementById("queue_container");
         queueContainer.innerHTML = "";

         // Get templates
         const orderTemplate = document.getElementById("order_template");
         const pizzaTemplate = document.getElementById("pizza_template");

         // Populate each order using the template
         data.queue.forEach((order) => {
            const orderClone = orderTemplate.content.cloneNode(true);
            orderClone.querySelector(".order_number").textContent =
               order.orderId;

            // Populate pizzas within each order
            const pizzaList = orderClone.querySelector(".pizza_list");
            for (const [pizza, quantity] of Object.entries(order.pizzas)) {
               const pizzaClone = pizzaTemplate.content.cloneNode(true);
               pizzaClone.querySelector(".pizza_name").textContent = pizza;
               pizzaClone.querySelector(".pizza_quantity").textContent =
                  quantity;
               pizzaList.appendChild(pizzaClone);
            }

            // Append the completed order to the container
            queueContainer.appendChild(orderClone);
         });
      } catch (error) {
         console.error("Error fetching orders:", error);
      }
   }

   // Initial fetch and set interval to refresh every 5 seconds
   fetchQueue();
   setInterval(fetchQueue, 5000);
});
