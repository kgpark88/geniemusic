<template>
  <v-layout row wrap text-center>
    <v-flex xs12 >
      <v-parallax id="parallax" :src="require('@/assets/discovery.jpg')" height="800" >
        <v-layout column align-center justify-center class="white--text">
          <h1 id="titleText" class="red--text mb-2 display-3 font-weight-bold font-italic">뮤직앱 리뷰분석 AI 서비스</h1>
          <div class="deep-purple--text text--lighten-3 subheading mb-3 headline font-weight-bold">
             Collect Review Data & Review AI Analysis
          </div>

          <div class="text-center ma-10">
            <v-btn class="mx-2 ma-1" x-large color="blue body-1" dark @click="classifier">데이터 수집</v-btn>
            <v-btn class="mx-2 ma-1" x-large color="blue body-1" dark @click="ocr">리뷰 AI 분석</v-btn>
            <v-btn class="mx-2 ma-1" x-large color="blue body-1" dark @click="dashboard">대시보드</v-btn> 
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
      classifier: function () {
        this.$router.push('/data');
      },      
      ocr: function () {
        this.$router.push('/anaysis');
      },
      dashboard: function () {
        this.$router.push('/dashboard');
      },
      about: function () {
        this.$router.push('/about');
      },             
    },
  }
</script>
