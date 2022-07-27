<template>
  <div>
    <v-container class="text-xs-center">
      <v-card class="mx-auto" max-width="400">
        <v-img class="white--text align-end" height="200px"
          :src="require('@/assets/docks.jpg')"
        >
          <v-card-title>{{ first_name }}님의 정보</v-card-title>
        </v-img>

        <v-layout row wrap >  
          <v-flex xs4>
            <v-card-text class="text--primary ml-2">회원권한</v-card-text>
          </v-flex>
          <v-flex xs8>
            <v-card-text class="text--primary">{{ member_type_str }}</v-card-text>
          </v-flex>

          <v-flex xs4>
            <v-card-text class="text--primary ml-2">이메일</v-card-text>
          </v-flex>
          <v-flex xs8>
            <v-card-text class="text--primary">{{ email }}</v-card-text>
          </v-flex>
                  

          <v-flex xs4>
            <v-card-text class="text--primary ml-2">소속기관</v-card-text>
          </v-flex>
          <v-flex xs8>
            <v-card-text class="text--primary">{{ company }}</v-card-text>
          </v-flex>


          <v-flex xs4>
            <v-card-text class="text--primary ml-2">부서</v-card-text>
          </v-flex>
          <v-flex xs8>
            <v-card-text class="text--primary ml-2">{{ department }}</v-card-text>
          </v-flex>


          <v-flex xs4>
            <v-card-text class="text--primary ml-2">전화번호</v-card-text>
          </v-flex>
          <v-flex xs8>
            <v-card-text class="text--primary">{{ phone }}</v-card-text>
          </v-flex>

        </v-layout>


        <v-card-actions>
          <v-btn color="orange" text @click="home">Home</v-btn>
          <v-btn color="orange" text @click="password_dialog=true">
            비밀번호변경
          </v-btn>
          <v-btn color="orange" text @click="userinfo_dialog=true">
            회원정보수정
          </v-btn>
          <v-btn color="orange" text @click="sign_out=true">
            회원탈퇴
          </v-btn>
        </v-card-actions>
      </v-card>

      <v-dialog v-model="password_dialog" max-width="500px">
        <v-card>
          <v-card-title>
            <span class="headline">비밀번호 변경</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    v-model="password"
                    prepend-icon="lock"
                    :append-icon="show1 ? 'visibility' : 'visibility_off'"
                    :type="show1 ? 'text' : 'password'"
                    name="password"
                    label="기존 비밀번호"
                    hint="영문자, 숫자, 특수기호 조합 8자리 이상"
                    @click:append="show1 = !show1"
                  ></v-text-field>
                  <v-text-field
                    v-model="new_password"
                    prepend-icon="lock"
                    :append-icon="show2 ? 'visibility' : 'visibility_off'"
                    :rules="passwordRules"
                    :type="show2 ? 'text' : 'password'"
                    name="password"
                    label="신규 비밀번호"
                    hint="영문자, 숫자, 특수기호 조합 8자리 이상"
                    @click:append="show2 = !show2"
                  ></v-text-field>

                  <v-text-field
                    v-model="password_confirmation"
                    prepend-icon="lock" 
                    :append-icon="show3 ? 'visibility' : 'visibility_off'"
                    :type="show3 ? 'text' : 'password'"
                    name="password_confirmation"
                    label="신규 비밀번호(확인)"
                    hint="영문자, 숫자, 특수기호 조합 8자리 이상"
                    class="input-group--focused"
                    @click:append="show3 = !show3"
                    :error-messages='paswordMatchError()'
                    required>
                  </v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" dark @click="password_dialog=false">취소</v-btn>
            <v-btn color="blue darken-1" dark 
              :disabled="!valid" 
              @click="change_password">
              비밀번호 변경
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>


      <v-dialog v-model="userinfo_dialog" max-width="500px">
        <v-card>
          <v-card-title>
            <span class="headline">내정보 수정</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    v-model="password"
                    prepend-icon="lock"
                    :append-icon="show1 ? 'visibility' : 'visibility_off'"
                    :type="show1 ? 'text' : 'password'"
                    name="password"
                    label="비밀번호"
                    @click:append="show1 = !show1">
                  </v-text-field>
                  <v-text-field prepend-icon="contact_mail" label="이메일"
                    v-model="email" :rules="emailRules" maxlength="50" required>
                  </v-text-field>  
                  <v-text-field prepend-icon="business" name="company" label="소속기관"
                    v-model="company" maxlength="50" required>
                  </v-text-field> 
                  <v-text-field prepend-icon="work" label="부서"
                    v-model="department" maxlength="50" required>
                  </v-text-field>
                  <v-text-field prepend-icon="contact_phone" label="전화번호"
                    v-model="phone" :rules="phoneRules" maxlength="50" required>
                  </v-text-field>
                  <v-text-field prepend-icon="supervisor_account" label="신청권한" readonly
                    v-model="member_type_str" >
                  </v-text-field>
                  <v-select v-model="member_type" :items="member_types" label="신청권한 선택"
                  prepend-icon="supervisor_account"  required>
                  </v-select>                                       
                </v-col>
              </v-row>

            </v-container>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" dark @click="userinfo_dialog=false">취소</v-btn>
            <v-btn color="blue darken-1" dark 
              :disabled="!valid" 
              @click="change_userinfo">
              내정보 수정
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>


      <v-dialog v-model="signout_dialog" max-width="500px">
        <v-card>
          <v-card-title>
            <span class="headline">회원 탈퇴</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    v-model="password"
                    prepend-icon="lock"
                    :append-icon="show1 ? 'visibility' : 'visibility_off'"
                    :type="show1 ? 'text' : 'password'"
                    name="password"
                    label="비밀번호"
                    hint="영문자, 숫자, 특수기호 조합 8자리 이상"
                    @click:append="show1 = !show1"
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" dark @click="signout_dialog=false">취소</v-btn>
            <v-btn color="blue darken-1" dark 
              :disabled="!valid" 
              @click="signout">
              회원탈퇴
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>




    </v-container>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data: () => ({
    password_dialog: false,
    userinfo_dialog: false,
    signout_dialog: false,
    valid: true,
    show1: false,
    show2: false,    
    show3: false,    
    username: '',
    password: '',
    new_password: '',
    password_confirmation: '',
    passwordRules: [
      v => !!v || '비밀번호를 입력하세요.',
      v => v.length >= 8 || '비밀번호는 8자리 이상입니다.'
    ],
    first_name: '',
    email: '',
    emailRules: [
      v => !!v || 'E-mail 주소를 입력하세요.',
      v => /.+@.+/.test(v) || '유효한 E-mail 주소를 입력하세요.'
    ],    
    member_type: 1,
    member_types: [
      {'value': 1, 'text':'멤버'},
      {'value': 2, 'text':'PL'},
      {'value': 3, 'text':'PM'},
      {'value': 4, 'text':'PMO'},
      {'value': 5, 'text':'임원'}
    ],

    company: '',
    department: '',
    phone: '',  
    phoneRules: [
      v => !!v || '전화번호를 입력하세요.',
    ],
  }),
  created: function () {
    this.get_user_info()
  },
  methods: {
    home () {
      // console.log("click home menu in the toolbar ")
      this.$emit('home')
    },     
    get_user_info(){
      let self = this
      let status = self.$store.getters.authStatus
      if(status == 'success'){
        self.username = self.$store.getters.username
        let url = process.env.VUE_APP_API_SERVER + '/userinfo'     
        let post_data = { "username": self.username}
        axios.post(url, post_data)
        .then(response => {
          self.first_name = response.data.user_info['first_name']
          self.email = response.data.user_info['email']
          self.member_type = response.data.user_info['member_type']
          self.member_type_str = self.member_types[self.member_type]
          self.company = response.data.user_info['company']
          self.department = response.data.user_info['department']
          self.phone = response.data.user_info['phone']
        })
      }else{
        self.$store.dispatch("logout")  
        self.$router.push('/')  
        self.$swal({
          type: 'info',
          title: '로그인을 하세요.',
        });       
      }      
    },
    paswordMatchError() { 
      return (this.new_password === this.password_confirmation) ? '' : '비밀번호 입력이 일치하지 않습니다.'
    },
    change_password() {
      let self = this
      let url = process.env.VUE_APP_API_SERVER + '/change-password'
      let post_data = { 
        'username': self.username,
        'password': self.password,
        'new_password': self.new_password,
      }
      axios.post(url, post_data)
      .then(response => {
        let result = response.data.result
        self.$swal({
          type: result,
          title: response.data.message,
        }); 
        if(result=="success"){
          self.$emit('home')
          self.$store.dispatch("logout")
        }
      })
    },
    change_userinfo() {
      let self = this
      let url = process.env.VUE_APP_API_SERVER + '/change-userinfo'
      let post_data = { 
        'username': self.username,
        'password': self.password,
        'email': self.email,
        'member_type': self.member_type,
        'company': self.company,
        'department': self.department,
        'phone': self.phone,
      }
      axios.post(url, post_data)
      .then(response => {
        let result = response.data.result
        self.$swal({
          type: result,
          title: response.data.message,
        }); 
        if(result=="success"){
          self.password = ''
          self.userinfo_dialog = false
          self.get_user_info()
        }
      })
    },
    signout() {
      let self = this
      let url = process.env.VUE_APP_API_SERVER + '/signout'
      let post_data = { 
        'username': self.username,
        'password': self.password
      }
      axios.post(url, post_data)
      .then(response => {
        let result = response.data.result
        self.$swal({
          type: result,
          title: response.data.message,
        }); 
        if(result=="success"){
          self.$emit('home')
          self.$store.dispatch("logout")
        }
      })
    },

  }  
};
</script>