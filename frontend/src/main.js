import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from "./router"
import VueMoment from 'vue-moment'
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';
import ECharts from 'vue-echarts'
import { use } from 'echarts/core'


// import ECharts modules manually to reduce bundle size
import {
  CanvasRenderer
} from 'echarts/renderers'
import {
  LineChart,
  BarChart,
  PieChart,
  ScatterChart,
  RadarChart,
  GraphChart,
} from 'echarts/charts'
import {
  GridComponent,
  TooltipComponent
} from 'echarts/components'

use([
  CanvasRenderer,
  GridComponent,
  TooltipComponent,
  LineChart,
  BarChart,
  PieChart,
  ScatterChart,
  RadarChart,
  GraphChart,
]);

// register globally (or you can do it locally)
Vue.component('v-chart', ECharts)

Vue.config.productionTip = false

Vue.use(VueMoment)
Vue.use(VueSweetalert2);

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
