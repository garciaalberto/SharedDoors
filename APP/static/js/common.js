function displayPrice(){
    type = $('[name="type"]').val();
    if (type === 'Payment') {
        $('#payment_price').css('display', 'inline-block');
    }
    else {
        $('#payment_price').css('display', 'none');
        $('#price').val(0);
    }
}