$(document).ready(function() {
    // replace anchor-link
    $('a.anchor-link').html('<i class="fas fa-link"></i>');

    // remove prompts
    $('div.prompt').remove();

    // on click select to unselected and back 
    $('div.cell.code_cell').on('click', function(){
        $('div.cell.code_cell').removeClass('selected').addClass('unselected');
        $(this).removeClass('unselected').addClass('selected');
    });

    // TODO: on "Run" click jump to the next cell
    // $('div.cell.code_cell.selected').find( "button" ).on('click', function() {
    //    alert('clicked');
    // });

    // TODO: double click on output -> disable it
});