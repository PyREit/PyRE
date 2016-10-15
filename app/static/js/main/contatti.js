function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

var contact_form = document.forms["contact-form"];
$(document).on('submit', contact_form, function(e) {
    var fields = ["nome", "cognome", "email", "messaggio"];
    fields.forEach(function(field) {
        var parent = contact_form[field].parentNode;
        if (!contact_form[field].value || ((field == 'email') && !validateEmail(contact_form[field].value))){
                parent.classList.remove("has-error");
                parent.classList.add("has-error");
            e.preventDefault();
        }
        else {
            parent.classList.remove("has-error");

        }
    });

});