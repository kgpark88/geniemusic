<template>
  <v-layout row wrap text-center>
    <v-flex xs12 >
      <v-parallax id="parallax" :src="require('@/assets/music.jpg')" height="800" >
        <v-layout column align-center justify-center class="white--text">
          <h1 id="titleText" class="white--text mb-2 display-3 font-weight-bold font-italic">뮤직앱 리뷰분석 AI 서비스</h1>
          <div class="black--text text--lighten-3 subheading mb-3 headline font-weight-bold">
             Collect Review Data & Review AI Analysis
          </div>

          <div class="text-center ma-10">
            <v-btn class="mx-2 ma-1" x-large color="blue body-1" dark @click="data_collect">데이터수집</v-btn>
            <v-btn class="mx-2 ma-1" x-large color="blue body-1" dark @click="search">리뷰조회</v-btn>
            <v-btn class="mx-2 ma-1" x-large color="blue body-1" dark @click="review_analysis">분석차트</v-btn> 
            <v-btn class="mx-2 ma-1" x-large color="blue body-1" dark @click="keyword_analysis">AI분석</v-btn> 
            <v-btn class="mx-2 ma-1" x-large color="blue body-1" dark @click="about">Contact</v-btn>
          </div>

        </v-layout>
      </v-parallax>
    </v-flex>
  </v-layout>
</template>


<script>
  export default {
    methods: {
      data_collect() {
        this.$router.push('/data');
      },      
      search () {
        this.$router.push('/search');
      },  
      review_analysis() {
        this.$router.push('/review-analysis');
      },
      keyword_analysis() {
        this.$router.push('/keyword-analysis');
      },      
      dashboard() {
        this.$router.push('/dashboard');
      },
      about() {
        this.$router.push('/about');
      },             
    },
  }
</script>
