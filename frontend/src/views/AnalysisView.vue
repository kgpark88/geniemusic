<template>
  <v-container class="lighten-5">

    <v-row no-gutters class="ma-6">
      <v-col cols="12" md="2" lg="2">
        <v-menu
          ref="menu1"
          v-model="menu1"
          :close-on-content-click="false"
          :return-value.sync="from_dt"
          transition="scale-transition"
          offset-y
        >
          <template v-slot:activator="{ on }">
            <v-text-field 
              v-model="from_dt"
              readonly
              v-on="on"
              hide-details
              class="white"
              outlined
              label="From"                
            ></v-text-field>
          </template>
          <template>
            <v-row justify="space-around">
              <v-date-picker 
                v-model="from_dt" 
                :first-day-of-week="0"
                locale="ko-kr"  
                @input="$refs.menu1.save(from_dt)"
              >
              </v-date-picker>
            </v-row>
          </template>
        </v-menu>  
      </v-col>

      <v-col cols="12" md="2" lg="2">
        <v-menu
          ref="menu2"
          v-model="menu2"
          :close-on-content-click="false"
          :return-value.sync="to_dt"
          transition="scale-transition"
          offset-y
        >
          <template v-slot:activator="{ on }">
            <v-text-field 
              v-model="to_dt"
              readonly
              v-on="on"
              hide-details
              class="white"
              outlined
              label="To"                 
            ></v-text-field>
          </template>
          <template>
            <v-row justify="space-around">
              <v-date-picker 
                v-model="to_dt" 
                :first-day-of-week="0"
                locale="ko-kr"  
                @input="$refs.menu2.save(to_dt)"
              >
              </v-date-picker>
            </v-row>
          </template>
        </v-menu> 
      </v-col>

      <v-col cols="12" md="2" lg="2">
        <v-btn
          class="ma-2"
          color="primary"
          @click="review_rating();review_analysis();"
        >
          리뷰 AI 분석
        </v-btn>
      </v-col> 
    </v-row>

    <v-row no-gutters>
      <v-col cols="12" sm="6">
        <v-layout align-center justify-center>
          <div class="text-h6 font-weight-medium">리뷰 별점</div>
        </v-layout>
        <v-card class="ma-2" flat tile>
          <v-chart :options="rating_chart" autoresize />
        </v-card>
      </v-col>   

      <v-col cols="12" sm="6">
        <v-layout align-center justify-center>
          <div class="text-h6 font-weight-medium">리뷰 감성 분포</div>
        </v-layout>
        <v-card class="ma-2" flat tile>
          <v-chart :options="pie_chart" autoresize />
        </v-card>
      </v-col>    
    </v-row>

    <v-row no-gutters class="ma-6">
      <v-col cols="12" sm="6">
        <v-card class="ma-2" flat tile>
          <v-layout align-center justify-center>
            <div class="text-h6 font-weight-medium">리뷰 긍정 키워드</div>
          </v-layout>
          <v-chip v-for="(item, i) in positive_word" :key="i" ripple 
            class="ma-2" color="primary" outlined pill>
            {{ item }}
          </v-chip>              
        </v-card>
      </v-col>
      <v-col cols="12" sm="6">
        <v-card class="ma-2" flat tile>
          <v-layout align-center justify-center>
            <div class="text-h6 font-weight-medium">리뷰 부정 키워드</div>
          </v-layout>
          <v-chip v-for="(item, i) in negative_word" :key="i" ripple 
            class="ma-2" color="#EC407A" outlined pill>
            {{ item }}
          </v-chip>            
        </v-card>
      </v-col>  
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'
import ECharts from '@/components/ECharts.vue'
import 'echarts/lib/component/title'
import 'echarts/lib/component/legend'
import 'echarts/lib/component/legendScroll'
import 'echarts/lib/component/tooltip'
import 'echarts/lib/component/toolbox'
import 'echarts/lib/chart/bar'
import 'echarts/lib/chart/line'
import 'echarts/lib/chart/scatter'
import 'echarts/lib/chart/effectScatter'
import 'echarts/lib/chart/pie'
import 'echarts/lib/chart/radar'

export default {
  components: {
    'v-chart': ECharts
  },  
  data: () => ({ 
    from_dt: '',
    to_dt: '',
    menu1: false,
    menu2: false,
    loading: false,
    rating_avg: 0,
    total: 0,
    positive: 0,
    negative: 0,
    positive_word: null,
    negative_word: null,
    rating_chart: null,
    pie_chart: null,
  }),
  created: function () {
    this.from_dt = this.$moment().set('month', 0).startOf('month').format('YYYY-MM-DD')
    this.to_dt   = this.$moment().set('month', 11).endOf('month').format('YYYY-MM-DD')    
    this.review_rating()
    this.review_analysis()
  },
  methods: { 
    review_rating(){
      let url = process.env.VUE_APP_API_SERVER + '/review/review-rating'
      let post_data = {
        from_dt: this.from_dt, 
        to_dt: this.to_dt,    
      }
      axios.post(url, post_data).then((response) => {
        this.rating_avg = response.data.rating_avg
        this.rating_chart = {
          legend: {},
          tooltip: {},
          xAxis: {type: 'value'},
          yAxis: {
            type: 'category',
            data: ['1점', '2점', '3점', '4점', '5점']
          },
          series: [
            {
              data: response.data.rating,
              type: 'bar',
              itemStyle:{
                color: '#EC407A',
              },  
              showBackground: true,
              backgroundStyle: {
                color: 'rgba(180, 180, 180, 0.2)'
              }
            }
          ]
        },
        this.pie_chart =  {
          title: [{         
            text: response.data.total,
            x: 'center',
            y: 'center',
          }],      
          tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
          },
          legend: {
            bottom: '5%',
            left: 'center'
          },
          series: [
            {
              name: '',
              type: 'pie',
              radius: ['25%', '75%'],
              avoidLabelOverlap: false,
              label: {
                position: 'inner',
                color: "white",
                fontSize: 20,
                formatter: '{d}%'
              },          
              data: [
                {'value': response.data.positive, 'itemStyle': {'color': '#3399FF'}},
                {'value': response.data.negative, 'itemStyle': {'color': '#FF0066'}}
              ],
              itemStyle: {
                emphasis: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
              }
            }
          ]
        }
      }).catch((error) => {
        console.log(error)
      })
    },
    async review_analysis(){
        this.positive_word = null
        this.negative_word = null
      let url = process.env.VUE_APP_API_SERVER + '/review/review-analysis'
      let post_data = {
        from_dt: this.from_dt, 
        to_dt: this.to_dt,    
      }
      try {
        const response = await axios.post(url, post_data)
        this.loading = false
        this.positive_word = response.data.positive_word
        this.negative_word = response.data.negative_word        
      } catch (err) {
        this.loading = false
        console.log(err)
      }
    }
  }
}

</script>


