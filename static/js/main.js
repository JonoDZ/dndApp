  $(function() {

  	//ON REROLL
    $('#rerollAll').bind('click', function() {

   	  //NPC GEN

   	  //get selected races to gen
	  var selected = "";
      $('#npcsToGen input:checked').each(function() {
        selected = selected + "," + String($(this).attr('name'));
      });
      //get the NPC Quantity
      $.getJSON('/regenNpcs', {
       npcQuant: $('input[name="npcGenQuant"]').val(),
       charList: selected,
      }, function(data) {
      	$("#npcTable").empty();
        $("#npcTable").append(data);
      });

      //BUILDING GEN
      var selected = "";
      $('#buildingsToGen input:checked').each(function() {
        selected = selected + "," + String($(this).attr('name'));
      });
      $.getJSON('/regenBuildings', {
        a: selected,
      }, function(data) {
      	$("#buildingsTable").empty();
        $("#buildingsTable").append(data);
      });
    return false;

    });
  });

 $(function(){

    $("#citySize li a").click(function(){

      $("#citySizeText").text($(event.target).text());
   });

});
  