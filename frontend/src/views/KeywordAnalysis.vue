<template>
  <v-container class="lighten-5">

    <v-row no-gutters class="ma-6">
      <v-col cols="12" md="4" lg="4">
        <v-select
          v-model="app_name"
          :items="app_names"
          menu-props="auto"
          hide-details
          class="white"
          outlined
          label="앱이름"
        >
        </v-select>
      </v-col> 
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
          large
          @click="review_analysis();"
        >
          분석
        </v-btn>
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
    <v-row>
      <v-layout align-center justify-center>
        <v-dialog v-model="process_dialog" hide-overlay persistent :width="max_width" >
          <v-card color="primary" dark>
            <v-progress-linear
              :color="progress_color"
              indeterminate
              rounded
              height="150"
            >
              <v-card-text 
                class="text-h3 justify-center font-weight-bold white--text"  

              > 
                {{progress_text}}({{timer_str}})
              </v-card-text>
            </v-progress-linear>
          </v-card>
        </v-dialog>
      </v-layout>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data: () => ({ 
    app_name: '지니뮤직',
    app_names: ['지니뮤직','멜론','유튜브뮤직'],
    progress_text : 'AI 리뷰분석',
    progress_color : 'deep-purple accent-4',
    process_dialog: false,
    max_width: '600px',
    disabled: false,
    timer: null,
    timer_str: '',
    from_dt: '',
    to_dt: '',
    menu1: false,
    menu2: false,
    positive: 0,
    negative: 0,
    positive_word: null,
    negative_word: null,
  }),
  created: function () {
    // this.from_dt = this.$moment().set('month', 0).startOf('month').format('YYYY-MM-DD')
    // this.to_dt   = this.$moment().set('month', 11).endOf('month').format('YYYY-MM-DD')    
    this.from_dt = new Date().toISOString().substr(0, 7) + '-01'
    this.to_dt = new Date().toISOString().substr(0, 10)
    this.review_analysis()
  },
  watch: {
    process_dialog(val) {
      if (!val) return;
      setTimeout(() => (this.process_dialog = false), 200000);
    }
  }, 
  mounted() {
    if(this.timer != null){
      this.timer_stop(this.timer);
        this.timer = null;
    }
  },
  methods: { 
    timer_start() {
      // 1초에 한번씩 start 호출
      this.timer_counter = 0;
      var interval = setInterval(() => {
        this.timer_counter++
        this.timer_str = this.pretty_time();
      }, 1000);
      return interval;
    },
    timer_stop(timer) {
      clearInterval(timer);
      this.timer_counter = 0;
    },
    pretty_time: function() {
      // 시간 형식으로 변환 리턴
      let time = this.timer_counter / 60;
      let minutes = parseInt(time);
      let secondes = Math.round((time - minutes) * 60);
      return (
        minutes.toString().padStart(2, "0") +
        "분" +
        secondes.toString().padStart(2, "0") + "초"
      );
    },  
    async review_analysis(){
      this.timer_start()
      this.positive_word = null
      this.negative_word = null
      this.process_dialog = true
      let url = process.env.VUE_APP_API_SERVER + '/review/review-analysis'
      let post_data = {
        app_name : this.app_name,
        from_dt: this.from_dt, 
        to_dt: this.to_dt,    
      }
      try {
        const response = await axios.post(url, post_data)
        this.timer_stop()
        this.process_dialog = false
        this.positive_word = response.data.positive_word
        this.negative_word = response.data.negative_word      
      } catch (err) {
        this.timer_stop()
        this.process_dialog = false
        console.log(err)
      }
    }
  }
}

</script>


