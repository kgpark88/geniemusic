<template slot="items" slot-scope="props">
  <v-card app  color="white">
    <v-toolbar class="pa-0 ma-0">
      <v-btn text to="/">
        <v-card-text class="title font-weight-bold">홈</v-card-text>
      </v-btn>

      <v-btn text to="/data">
        <v-card-text class="title font-weight-bold">데이터 수집</v-card-text> 
      </v-btn>

      <v-btn text to="/search">
        <v-card-text class="title font-weight-bold">리뷰 분석</v-card-text> 
      </v-btn>

      <v-btn text to="/analysis">
        <v-card-text class="title font-weight-bold">리뷰 AI 분석</v-card-text> 
      </v-btn>

      <v-btn text to="/dashboard">
        <v-card-text class="title font-weight-bold">대시보드</v-card-text>
      </v-btn>

      <v-spacer></v-spacer>

      <div class="pl-2">
        <v-tooltip top>
          <template v-slot:activator="{ on }">
            <v-btn icon to="/about" v-on="on">
              <v-icon>mdi-information</v-icon>     
            </v-btn>   
          </template>
          <span>About</span>
        </v-tooltip> 
      </div>   

    </v-toolbar>
  </v-card>   
</template>

