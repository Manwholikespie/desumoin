var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        authors: '',
        text: '',
        context: ''
    },
    computed: {
        preview: function () {
            if (!this.authors || !this.text) {
                return '';
            }
            var out = this.text + '\n~ ' + this.authors;
            if (this.context) {
                out += ', ' + this.context;
            }
            return out;
        }
    }
});