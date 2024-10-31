function incrementPizzaQuantity(pizza) {
   const inputField = document.getElementById(`${pizza}_quantity`);
   let currentQuantity = parseInt(inputField.value);
   if (currentQuantity < 10) {
      currentQuantity += 1;
      inputField.value = currentQuantity;
   } else {
      return;
   }
}

function decrementPizzaQuantity(pizza) {
   const inputField = document.getElementById(`${pizza}_quantity`);
   let currentQuantity = parseInt(inputField.value);
   if (currentQuantity > 0) {
      currentQuantity -= 1;
      inputField.value = currentQuantity;
   } else {
      return;
   }
}

async function submitOrder() {
   const orderedPizzas = {};
   const quantities = document.getElementsByClassName("quantity");

   for (let i = 0; i < quantities.length; i++) {
      if (quantities[i].value > 0) {
         let type = quantities[i].id.split("_")[0];
         let quantity = parseInt(quantities[i].value);
         orderedPizzas[type] = quantity;
      }
   }

   // Send the data to the server using fetch (POST request with JSON payload)
   const response = await fetch("/order", {
      method: "POST",
      headers: {
         "Content-Type": "application/json",
      },
      body: JSON.stringify(orderedPizzas),
   });

   // Instead of trying to get JSON, check if redirected
   if (response.redirected) {
      window.location.href = response.url; // Redirect to complete order page
   } else {
      // Handle the response if it's not a redirect
      alert("There was an error processing your order.");
   }
}
