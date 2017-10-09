$( '[data-role="ratingbar"]' )
   .ratingbar()
   .click(function() {

    // Grab value
    alert( $( this ).attr( 'data-value' ) );

    return false;
});
