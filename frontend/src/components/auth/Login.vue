<template>
  <form class="login" @submit.prevent="login">
    <v-content>
      <v-container style="position: relative;top: 13%;" class="text-xs-center">
        <v-layout align-center justify-center>
           <v-flex xs4 class="grey lighten-4">
            <v-card class="elevation-2">
              <v-toolbar dark color="light-blue lighten-2">
                <v-toolbar-title class="justify-center">로그인</v-toolbar-title>
                <v-spacer></v-spacer>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field prepend-icon="person" name="login" label="아이디"
                    v-model="username" type="text" placeholder="Username"
                    autofocus="autofocus" maxlength="150" id="id_username">
                  </v-text-field>
                  <v-text-field prepend-icon="lock" name="password" label="비밀번호" 
                    v-model="password" type="password"
                    placeholder="Password" id="id_password" >
                  </v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions class="justify-center">
                <v-btn class="primary" type="submit" >로그인</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>

  </form>
</template>

<script>

export default {
  data() {
    return {
      username: "",
      password: ""
    };
  },

  methods: {
    login: function() {
      let username = this.username;
      let password = this.password;
      this.$store
        .dispatch("login", { username, password })
        .then(() => this.$router.push("/"))
        .catch(err => console.log(err));
    }
  }
};
</script>
