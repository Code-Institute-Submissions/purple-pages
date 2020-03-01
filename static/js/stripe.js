// Stripe elements for subscription payments

function requestPayment(subscriptionFormData) {
    // Request payment intent and setup a payment form
    console.log(subscriptionFormData.payment-request-url.value)
    $.post(subscriptionFormData[1]['value'], subscriptionFormData[0].serialize())
}


let stripe = Stripe('pk_test_Tgy18iERVA1liKcyrLebR4sN00fdlqLNY0');
let stripeElements = stripe.elements();

// Create Stripe payment elements in payment form
$('#subscription-form').submit(function(subscriptionForm) {
    // Collect form data
    let subscriptionFormData = $(this).serializeArray()
    // Disable subscription form
    subscriptionForm.preventDefault();
    $('#subscription-form :input').prop('disabled', true)
    // Request payment intent with form data   
    requestPayment(subscriptionForm)
    
    // Generate and display the payment form
    let stripeStyle = {
      };
    let stripePaymentElements = stripeElements.create("card", {style:stripeStyle});
    stripePaymentElements.mount("#stripe-card-element");

    // Listen for stripe input validation errors and display  
    stripePaymentElements.addEventListener('change', ({error}) => {
        if (error) {
            $('#stripe-card-errors').text(error.message);
        } else {
            $('#stripe-card-errors').empty();
        }        
    });      
})

// Handle payment cancel button
$('#stripe-cancel').click(function(stripePaymentForm) {
    stripePaymentForm.preventDefault();
    // Clear payment form and reset subscription form
    //document.getElementById("subscription-form").reset();  
})

