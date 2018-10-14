function myAlert() {
    alert("Hello! I am an alert box!!");
}

function initialize() {
    var $form = $("form#recipe_search");
    console.log($form);
// debugger;
    $form.submit(function(event) {
    // debugger;
        console.log("triggered")
        myAlert();
        event.preventDefault();
    })
}


$( document ).ready(initialize)