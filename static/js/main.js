
  $(function() {
    $('a#regenBuildings').bind('click', function() {	

      var selected = "";
      $('#buildingsToGen input:checked').each(function() {
        selected = selected + "," + String($(this).attr('data-on'));
      });
      $.getJSON('/regenBuildings', {
        a: selected,
      }, function(data) {
		console.log(data)
		//$('#console-event').text(data);
      });
      return false;
    });
  });

  $(function() {
    $('a#calculate').bind('click', function() {

      $.getJSON('/redo', {
        a: $('input[name="a"]').val(),
      }, function(data) {
      	$("#NpcTable").empty();
        $("#NpcTable").append(data);
      });
      return false;
    });
  });

