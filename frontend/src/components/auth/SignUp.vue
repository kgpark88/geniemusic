<template>
  <v-form ref="form" v-model="valid" lazy-validation>
    <form class="login" @submit.prevent="signup">
      <div>
        <v-container class="text-xs-center">
          <v-layout align-center justify-center>
             <v-flex xs6 class="grey lighten-4">
              <v-card class="elevation-2">
                <v-toolbar dark color="light-blue lighten-2">
                  <v-toolbar-title class="justify-center">회원가입</v-toolbar-title>
                  <v-spacer></v-spacer>
                </v-toolbar>

                <v-container fluid grid-list-md>
                  <v-layout row wrap >                    
                    <v-flex xs12>
                      <v-text-field name="username" data-vv-name="username"
                      prepend-icon="person"  v-model="username" 
                      label="아이디" :maxlength="20" :counter="20" :rules="usernameRules"
                      hint="영문자, 숫자 조합 6자리 이상" required>
                      </v-text-field>                 
                    </v-flex>

                    <v-flex xs6>
                      <v-text-field
                        v-model="password"
                        prepend-icon="lock"
                        :append-icon="show1 ? 'visibility' : 'visibility_off'"
                        :rules="passwordRules"
                        :type="show1 ? 'text' : 'password'"
                        name="password"
                        label="비밀번호"
                        hint="영문자, 숫자, 특수기호 조합 8자리 이상"
                        @click:append="show1 = !show1"
                      ></v-text-field>
                    </v-flex>

                    <v-flex xs6>
                      <v-text-field
                        v-model="password_confirmation"
                        prepend-icon="lock" 
                        :append-icon="show2 ? 'visibility' : 'visibility_off'"
                        :type="show2 ? 'text' : 'password'"
                        name="password_confirmation"
                        label="비밀번호(확인)"
                        hint="영문자, 숫자, 특수기호 조합 8자리 이상"
                        class="input-group--focused"
                        @click:append="show2 = !show2"
                        :error-messages='paswordMatchError()'
                        required>
                      </v-text-field>
                    </v-flex>

                    <v-flex xs6>
                      <v-text-field prepend-icon="person" name="first_name" label="성함"
                        v-model="first_name" type="text" maxlength="50" id="id_first_name">
                      </v-text-field>            
                    </v-flex>
                    <v-flex xs6 d-flex>
                      <v-select v-model="member_type" :items="member_types" label="신청권한" 
                      :rules="[v => !!v || '신청권한을 선택하세요.']" 
                      prepend-icon="supervisor_account" required>
                      </v-select>                   
                    </v-flex>


                    <v-flex xs12>
                      <v-text-field prepend-icon="contact_mail" label="이메일"
                        v-model="email" :rules="emailRules" maxlength="50" required>
                      </v-text-field>  
                    </v-flex>
                      
                    <v-flex xs6>
                      <v-text-field prepend-icon="business" name="company" label="소속기관"
                        v-model="company" maxlength="50" required>
                      </v-text-field>                 
                    </v-flex>
                    <v-flex xs6>
                      <v-text-field prepend-icon="work" label="부서"
                        v-model="department" maxlength="50" required>
                      </v-text-field>                 
                    </v-flex>   

                    <v-flex xs6>
                      <v-text-field prepend-icon="contact_phone" label="전화번호"
                        v-model="phone" :rules="phoneRules" maxlength="50" required>
                      </v-text-field>              
                    </v-flex>

                    <v-flex xs12>
                      <v-checkbox
                        label="개인정보 보호에 동의합니다."
                        v-model="check_01"
                        :rules="[(v) => !!v || '개인정보 보호에 동의하여야 합니다']"
                      ></v-checkbox>
                    </v-flex>
                    
                  </v-layout>
                </v-container>
                <v-card-actions class="justify-center">
                  <v-btn :disabled="!valid" class="primary" type="submit" >회원가입</v-btn>
                  <v-btn class="primary" to="/" >HOME</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </div>
    </form>
  </v-form>
</template>


<script>
import axios from 'axios'

export default {
  data: () => ({
    valid: true,
    show1: false,
    show2: true,
    show3: false,
    show4: false,

    username: '',
    usernameRules: [
      v => !!v || 'ID를 입력하세요.',
      v => (v && v.length <= 20) || 'ID는 20자 이내입니다.',
    ],
    password: "",
    password_confirmation: "",
    passwordRules: [
      v => !!v || '비밀번호를 입력하세요.',
      v => v.length >= 8 || '비밀번호는 8자리 이상입니다.'
    ],
    first_name: "",
    email: '',
    emailRules: [
      v => !!v || 'E-mail 주소를 입력하세요.',
      v => /.+@.+/.test(v) || '유효한 E-mail 주소를 입력하세요.'
    ],
    member_type: '일반',
    member_types: [
      {'value': '일반', 'text':'일반'},
      {'value': '멤버', 'text':'프로젝트멤버'},
      {'value': '사업부서', 'text':'사업부서'},
      {'value': 'PL', 'text':'PL'},
      {'value': 'PM', 'text':'PM'},
      {'value': 'PMO', 'text':'PMO'},
      {'value': '팀장', 'text':'팀장'},
      {'value': '임원', 'text':'임원'},
    ],
    company: "",
    department: "",
    phone:"",  
    phoneRules: [
      v => !!v || '전화번호를 입력하세요.',
    ],
    check_01: false  

  }),
  methods: {
    // reset () {
    //   this.$refs.form.reset()
    // },  
    paswordMatchError() { 
      return (this.password === this.password_confirmation) ? '' : '비밀번호 입력이 일치하지 않습니다.'
    },
    signup: function() {
      let url = process.env.VUE_APP_API_SERVER + '/register' 
      let post_data = {
        username: this.username,
        password: this.password,
        first_name: this.first_name,
        email: this.email,
        member_type: this.member_type,
        company: this.company,
        department: this.department,
        phone: this.phone,
      };

      axios.post(url, post_data)
      .then(response => {
        this.$swal({
          timer: 2000,
          type: 'info',
          text: response.data["message"],
        })
        if(response.data["result"]==="success"){
          this.$router.push("/")
        }
      })
    }
  }
};
</script>