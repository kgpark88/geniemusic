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
          @change="get_reviews"
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
              label="To"                 
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
        <v-text-field
          v-model="search_word"
          outlined
          clearable
          hide-details
          @keypress.enter="get_reviews">
          <template v-slot:prepend-inner>
            <v-icon>search</v-icon>
          </template>
        </v-text-field>        
      </v-col>

      <v-col cols="12" md="2" lg="2">
        <v-btn
          class="ma-2"
          color="primary"
          large
          @click="get_reviews"
        >
          조회
        </v-btn>
      </v-col>

    </v-row>

    <v-row >
      <v-col cols="10">        
        <v-card-title>
          ◆ 리뷰 데이터
        </v-card-title>
      </v-col>
      <v-col cols="2">        
        <v-btn outlined color="teal lighten-1" x-large>
          <v-icon left>mdi-file-excel</v-icon>
          <download-excel
            class   = "btn btn-default"
            :data   = "reviews"
            :fields = "json_fields"
            worksheet = "리뷰데이터"
            :name    = "file_name">다운로드 
          </download-excel>
        </v-btn> 
      </v-col>        
    </v-row>


    <v-row no-gutters>
      <v-col cols="12" sm="12" md="12" class="pa-2">
        <v-card class="pa-2" outlined tile>
          <v-data-table 
            :headers="headers" 
            :items="reviews" 
            :page.sync="page"
            :items-per-page="itemsPerPage"
            hide-default-footer
            @page-count="pageCount = $event"
          >
          </v-data-table>  
           <div class="text-center pt-2">
            <v-pagination
              v-model="page"
              :length="pageCount"
            ></v-pagination>
          </div>         
        </v-card>
      </v-col>
    </v-row>

  </v-container>
</template>


<script>
import axios from 'axios'

export default {
  data: () => ({
    app_name: '지니뮤직',
    app_names: ['지니뮤직','멜론','유튜브뮤직'],
    file_name: "리뷰데이터.xls",
    from_dt: '',
    to_dt: '',
    search_word: '',
    menu1: false,
    menu2: false,
    page: 1,
    pageCount: 0,
    itemsPerPage: 10,
    reviews: [],
    headers: [
      // {'text': '리뷰ID', 'value': 'review_id', 'width': '200px'},
      {'text': '사용자', 'value': 'user_name', 'width': '200px'},
      {'text': '리뷰내용', 'value': 'content', 'width': '700px'},
      {'text': '별점', 'value': 'score', 'width': '100px'},
      {'text': '작성일', 'value': 'at', 'width': '100px'},
      {'text': '답변', 'value': 'reply_content', 'width': '700px'},
      {'text': '구분', 'value': 'source', 'width': '100px'}
    ],    
    json_fields: {
      '앱이름': 'app',
      '리뷰ID': 'review_id',
      '사용자': 'user_name',
      '리뷰내용': 'content',
      '별점': 'score',
      '작성일': 'at',
      '답변': 'reply_content',
      '구분': 'source'
    }    
  }), 
  created () {
    this.from_dt = this.$moment().set('month', 0).startOf('month').format('YYYY-MM-DD')
    this.to_dt   = this.$moment().set('month', 11).endOf('month').format('YYYY-MM-DD')
    this.get_reviews()
  },  

  methods: {
    get_reviews(){
      let url = process.env.VUE_APP_API_SERVER + '/review/list'
      let post_data = {
        app_name : this.app_name,
        search_word: this.search_word, 
        from_dt: this.from_dt, 
        to_dt: this.to_dt,        
      }
      axios.post(url, post_data).then((response) => {
          this.reviews = response.data.reviews
      }).catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>
