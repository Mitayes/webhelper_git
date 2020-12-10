var vue_field = new Vue({
  el: '#test',
  data() {
    return {
      message: null
    };
  },
  mounted() {
    axios
      .get('json_Search?search=u3')
//      .then(response => (this.message = response.data[0].quest_text));
      .then(response => (this.message = response.data));
  }
})