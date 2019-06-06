import Vue from 'vue'
import VueResource from 'vue-resource'

Vue.use(VueResource)

Vue.http.options.root = '/api'

import MyComponent from './MyComponent.vue'

const app = new Vue({
  el: '#app',
  components: {
    MyComponent,
  },
})
