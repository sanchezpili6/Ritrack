<template>
  <div>
    <AppBar login></AppBar>
    <div class="main">
      <v-card width="800px" height="400px" class="card" >
        <v-card-title class="options">SIGN UP</v-card-title>
        <v-card-text>
          <v-text-field v-model="name" :rules="nameRules" label="Name" outlined dense></v-text-field>
          <v-text-field v-model="email" :rules="emailRules" label="E-mail" outlined dense></v-text-field>
          <v-text-field v-model="password" type="password" class="password" label="Password" outlined dense></v-text-field>
        </v-card-text>
        <v-card-actions class="options">
          <v-btn color="#D46626" to="/login">I already have an account</v-btn>
          <v-btn color="#FFA625" @click="addUser">Sign Up</v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </div>
</template>

<script>
import {add_user} from "@/helpers/Services";
import AppBar from "@/components/AppBar";
export default {
  name: "SignUpView.vue",
  components:{
    AppBar
  },
  data:()=>{
    return{
      name: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      password: ''
    }
  },
  methods:{
    async addUser(){
      const data = {
        "name": this.name,
        "email": this.email,
        "password": this.password
      }
      await add_user(data).then(this.$router.replace('/lost'))
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
