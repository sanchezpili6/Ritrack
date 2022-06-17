<template>
  <v-app-bar
      color="#D46626"
      hide-on-scroll
  >
    <v-app-bar-nav-icon @click.stop="drawer = !drawer" class="hidden-md-and-up"></v-app-bar-nav-icon>
    <v-spacer></v-spacer>

    <v-btn icon v-show="!login" to="/lost" class="hidden-sm-and-down">
      <h2>Lost Pets</h2>
    </v-btn>

    <v-btn icon v-show="login" to="/" class="hidden-sm-and-down">
      <h2>About Us</h2>
    </v-btn>

    <v-spacer></v-spacer>

    <v-btn icon v-show="!login" to="/found" class="hidden-sm-and-down">
      <h2>Found Pets</h2>
    </v-btn>
    <v-btn icon v-show="login" to="/signup" class="hidden-sm-and-down">
      <h2>Sign up</h2>
    </v-btn>

    <v-spacer></v-spacer>

    <v-btn icon v-show="!login" to="/my-pets" class="hidden-sm-and-down">
      <h2>My Pets</h2>
    </v-btn>
    <v-btn icon v-show="login" to="/login" class="hidden-sm-and-down">
      <h2>Login</h2>
    </v-btn>

    <v-spacer></v-spacer>

    <v-btn icon v-show="!login" to="/profile" class="hidden-sm-and-down">
      <h2>Profile</h2>
    </v-btn>

    <v-spacer v-show="!login"></v-spacer>

    <v-btn icon v-show="!login" @click="logout" class="hidden-sm-and-down">
      <h2>Log out</h2>
    </v-btn>

    <v-spacer v-show="!login"></v-spacer>
  </v-app-bar>
</template>

<script>
import {logout} from "@/helpers/Services";
export default {
  name: "AppBar.vue",
  props:{
    login: Boolean
  },
  mounted() {
    if(localStorage.email){
      this.email = localStorage.email
    }
  },
  data:()=>{
    return{
      email: ''
    }
  },
  methods:{
    async logout(){
      const data = {"email": this.email}
      await logout(data).then(this.$router.replace('/'))
    }
  }
}
</script>

<style scoped>

</style>
