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
          @click="get_reviews"
        >
          리뷰 데이터 조회
        </v-btn>
      </v-col>

    </v-row>

    <v-row no-gutters>
      <v-col cols="12" sm="12" md="12" class="pa-2">
        <v-card class="pa-2" outlined tile>
          <v-data-table 
            :headers="headers" 
            :items="reviews" 
            :items-per-page="itemsPerPage"
          >
          </v-data-table>  
        </v-card>
      </v-col>
    </v-row>

  </v-container>
</template>


<script>
import axios from 'axios'

export default {
  data: () => ({
    from_dt: '',
    to_dt: '',
    menu1: false,
    menu2: false,
    itemsPerPage: 10,
    reviews: [],
    headers: [
      {'text': '리뷰', 'value': 'content', 'width': '800px'},
      {'text': '별점', 'value': 'score', 'width': '100px'},
      {'text': '작성일', 'value': 'at', 'width': '100px'},
      {'text': '구분', 'value': 'source', 'width': '100px'},
    ],    
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
        search_word: '', 
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
