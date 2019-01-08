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
        },
        submit_data: function () {
            var d_authors = this.authors.split(',').map(
                s => s.trim().toLowerCase()
            ).filter(s => s);
            var d_text = this.text.trim();
            var d_context = this.context.trim();

            return {
                'authors': d_authors,
                'text': d_text,
                'context': d_context
            }
        }
    },
    methods: {
        submit: function () {
            if (!this.preview) {
                alert('Provide some text and an author first.')
                return;
            }
            $.post('/submit', this.submit_data, function (data) {
                // success
            }).done(function (data) {
                // done
            }).fail(function (data) {
                // failure
                console.log('An error occurred while submitting the quote.')
                console.log(data)
            });

            // Clear the data.
            this.authors = ''
            this.text = ''
            this.context = ''
        }
    }
});