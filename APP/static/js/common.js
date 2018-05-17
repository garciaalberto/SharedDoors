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

function textToClipboard (text) {
    let dummy = document.createElement("textarea");
    document.body.appendChild(dummy);
    dummy.value = text;
    dummy.select();
    document.execCommand("copy");
    document.body.removeChild(dummy);
}