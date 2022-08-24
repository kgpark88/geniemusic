<template>
  <div>  
 
    <v-card class="mx-auto lighten-5 ma-10" max-width="800px">
      <v-system-bar height="60" dark color="#2962FF">
        <v-icon large>mdi-checkbox-marked-outline</v-icon>
        <span class="headline">뮤직앱 리뷰데이터 수집(구글 앱스토어)</span>          
      </v-system-bar>
      <v-row class='ma-2'>
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
          <v-btn
            large
            class="ma-2"
            color="primary"
            @click="data_collect"
            :disabled="process_dialog"
          >
            리뷰 데이터 수집
          </v-btn>    
        </v-col>
      </v-row>      
    </v-card>

    <v-card class="mx-auto lighten-5 ma-10" max-width="800px">
      <v-system-bar height="60" dark color="#42A5F5">
        <v-icon large>mdi-checkbox-marked-outline</v-icon>
        <span class="headline">리뷰 데이터 업로드</span>          
      </v-system-bar>
  
      <v-row class='ma-2'>
        <v-col cols="12" md="4">
          <v-file-input
            v-model="chosenFile"
            accept="csv"
            label="리뷰 데이터(*.csv)"
            outlined
            large
          ></v-file-input>
        </v-col>

        <v-col cols="12" md="4">
          <v-btn
            large
            class="ma-2"
            color="primary"
            @click="data_upload"
            :disabled="process_dialog"
          >
            리뷰 데이터 업로드
          </v-btn>          
        </v-col>  
      </v-row>
    </v-card>
      
      
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
              @click="process_dialog=false"
            > 
              {{progress_text}}
            </v-card-text>
          </v-progress-linear>
        </v-card>
      </v-dialog>
    </v-layout>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  data: () => ({  
    app_name: '지니뮤직',
    app_names: ['지니뮤직','멜론','유튜브뮤직'],
    chosenFile: null,
    progress_text : 'Processing...',
    progress_color : 'deep-purple accent-4',
    process_dialog: false,
    max_width: '400px',
    disabled: false,
  }),
  watch: {
    process_dialog(val) {
      if (!val) return;
      setTimeout(() => (this.process_dialog = false), 200000);
    }
  }, 
  methods: {
    async data_collect() {
      this.process_dialog = true
      let url = process.env.VUE_APP_API_SERVER + '/review/review-collect-google-appstore'
      let post_data = {
        app_name : this.app_name
      }
      try {
        const response = await axios.post(url, post_data)
        this.process_dialog = false
        this.$swal.fire({
          icon: response.data.info,
          title: response.data.result
        })      
      } catch (err) {
        this.process_dialog = false
        console.log(err)
      }
    },
    async data_upload() {
      if (this.chosenFile) {
        this.process_dialog = true
        let url = process.env.VUE_APP_API_SERVER + '/review/data-upload'
        let post_data = new FormData();
        post_data.append("file", this.chosenFile);
        try {
          const response = await axios.post(url, post_data)
          this.process_dialog = false
          this.$swal.fire({
            icon: response.data.info,
            title: response.data.result
          })      
        } catch (err) {
          this.process_dialog = false
          console.log(err)
        }
      } else {
        this.$swal.fire({
          icon: 'info',
          title: "CSV 파일을 선택 하세요."
        });
      }
    }
  }
}
</script>

