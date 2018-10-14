function deleteParentEntry(event) {
    this.parent("div").remove();
    event.preventDefault();
}

function initialize() {
    $("#ingredients").append("<button id='add'>+</button>")
    var $addButton = $("#add");
    $addButton.click(function(event) {
        var newIngredient = $(".ingredientTemplate").clone()
            newIndex = $(".ingredientSingle").length + 1;
        console.log(newIndex)
        newIngredient.find("input").each(function() {
            var oldName = $(this).attr("name")
            newName = oldName.replace("$index", newIndex)
            $(this).attr("name", newName)
        })
        newIngredient.attr("class", "ingredientSingle")
        newIngredient.attr("style", "")
        newIngredient.insertBefore($addButton)

        var deleteButton = newIngredient.find(".deleteIngredient")
        deleteButton.click(deleteParentEntry.bind())

        event.preventDefault();
    })
    var $deleteButton = $(".deleteIngredient").each(function() {
        $(this).click(deleteParentEntry.bind($(this)))
    });
}


$( document ).ready(initialize)