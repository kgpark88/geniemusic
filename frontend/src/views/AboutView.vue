<template>
  <v-card max-width="800" class="mx-auto grey lighten-5 ma-10" flat>
    <v-container class="grey lighten-5">
      <v-row>
        <v-col sm="12">
          <v-card>
            <v-img src="@/assets/dev.jpg">
            </v-img>


            <v-card-actions>                               
              <v-icon class="ma-2">mdi-contact-mail</v-icon>
              <p class="ma-2 light-blue--text font-weight-bold"><a href="mailto:danny.park@kt.com">kgpark88@gmail.com</a></p>
              <v-spacer></v-spacer>
              <v-icon class="ma-2">mdi-github-circle</v-icon>
              <p class="ma-2 light-blue--text font-weight-bold" ><a href="https://github.com/kgpark88">https://github.com/kgpark88</a></p> 
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<style>
  a {
    text-decoration: none;
  }
</style>

