  $(function() {
    $('#regenerateAll').bind('click', function() {

      $.getJSON('/regenNpcs', {
        a: $('input[name="a"]').val(),
      }, function(data) {
      	$("#npcTable").empty();
        $("#npcTable").append(data);
      });

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

  

