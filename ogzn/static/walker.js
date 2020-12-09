var vue_field = new Vue({
  el: '#vue_field',
  data: {
    message: 'Привет, Vue!',
    one: false,
    two: true,
  },
    methods: {
        swapButtons: function () {
          this.one = !this.one
          this.two = !this.one
        }
    }
})

