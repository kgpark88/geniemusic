<template>
  <div>  
 
    <v-card class="mx-auto lighten-5 ma-10" max-width="1400px">
      <v-system-bar height="60" dark color="deep-purple lighten-1">
        <v-icon large>mdi-checkbox-marked-outline</v-icon>
        <span class="headline">리뷰 데이터 수집</span>          
      </v-system-bar>
      <v-row no-gutters>
        <v-col cols="12">
        </v-col>
      </v-row>

      <v-row class='ma-2'>
        <v-col cols="12" md="4">
          <v-file-input
            v-model="chosenFile"
            accept="csv"
            label="리뷰 데이터 파일 업로드(*.csv)"
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
            데이터 저장
          </v-btn>          
        </v-col>  

        <v-col cols="12" md="4">
        </v-col> 
      </v-row>
    </v-card>
      
    <v-layout align-center justify-center>
      <v-dialog v-model="process_dialog" hide-overlay persistent width="400" >
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
    chosenFile: null,
    progress_text : '데이터 저장',
    progress_color : 'deep-purple accent-4',
    process_dialog: false,
    max_width: '400px',
    disabled: false,

    predicted_label:"",
    image_path:"",
  }),
  watch: {
    process_dialog(val) {
      if (!val) return;
      setTimeout(() => (this.process_dialog = false), 200000);
    }
  }, 
  methods: {

    async data_upload() {
      if (this.chosenFile) {
        this.predicted_label = ''
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

