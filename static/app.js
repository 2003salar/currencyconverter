document.addEventListener('DOMContentLoaded', function() {
    // validate forms using isvalid isnotvalid
    let inputs = document.getElementsByTagName('input');
    for (let i = 0; i < inputs.length; i++) {
        let input = inputs[i];
        input.addEventListener('input', function() {
            if (input.value == '') {
                this.classList.remove('is-valid')
                this.classList.add('is-invalid')
            }
            else {
                this.classList.remove('is-invalid')
                this.classList.add('is-valid')
            }
        });
    }

    let message = document.getElementsByTagName('textarea')[0];
    message.addEventListener('input', function () {
        if (this.value.length > 500 || this.value.length < 20) {
            this.classList.remove('is-valid');
            this.classList.add('is-invalid');
        }
        else {
            this.classList.remove('is-invalid')
            this.classList.add('is-valid')
        }
    });
});