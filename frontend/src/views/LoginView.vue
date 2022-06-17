<template>
  <div>
    <AppBar login></AppBar>
    <div class="main">
      <v-card width="800px" height="400px" class="card" >
        <v-card-title class="justify-center">
          <v-spacer></v-spacer>
          LOGIN
          <v-spacer></v-spacer>
        </v-card-title>
        <v-card-text>
          <v-text-field v-model="email"  label="E-mail" outlined dense></v-text-field>
          <v-text-field v-model="password" type="password" label="Password" outlined dense></v-text-field>
        </v-card-text>
        <v-card-actions class="options">
          <v-btn color="#D46626" to="/signup">I don't have an account</v-btn>
          <div></div>
          <v-btn color="#FFA625" @click="login">Continue</v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </div>
</template>

<script>
import AppBar from "@/components/AppBar";
import {login} from "@/helpers/Services";
export default {
  name: "LoginView.vue",
  components:{
    AppBar
  },
  watch: {
    email(newEmail) {
      localStorage.email = newEmail;
    }
  },
  data:()=>{
    return{
      email: '',
      password: '',
    }
  },
  methods:{
    async login(){
      const data = {"email": this.email, "password": this.password}
      await login(data).then(this.$router.replace('/lost'))
    }
  }
}
</script>

<style scoped>
  .options{
    display: flex;
    justify-content: space-evenly;
    flex-direction: row;
  }
  .main{
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    background-color: #645D53;
    position:absolute;
    top:60px;
    right:0px;
    bottom:0px;
    left:0px;
  }
  .card{
    border-radius: 3%;
  }
</style>
