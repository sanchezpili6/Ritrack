<template>
  <v-app-bar
      color="#D46626"
      hide-on-scroll
  >
    <v-spacer></v-spacer>

    <v-btn icon v-show="!login" to="/lost">
      <h2>Lost Pets</h2>
    </v-btn>

    <v-btn icon v-show="login" to="/">
      <h2>About Us</h2>
    </v-btn>

    <v-spacer></v-spacer>

    <v-btn icon v-show="!login" to="/found">
      <h2>Found Pets</h2>
    </v-btn>
    <v-btn icon v-show="login" to="/signup">
      <h2>Sign up</h2>
    </v-btn>

    <v-spacer></v-spacer>

    <v-btn icon v-show="!login" to="/my-pets">
      <h2>My Pets</h2>
    </v-btn>
    <v-btn icon v-show="login" to="/login">
      <h2>Login</h2>
    </v-btn>

    <v-spacer></v-spacer>

    <v-btn icon v-show="!login" to="/profile">
      <h2>Profile</h2>
    </v-btn>

    <v-spacer v-show="!login"></v-spacer>

    <v-btn icon v-show="!login" to="/">
      <h2>Log out</h2>
    </v-btn>

    <v-spacer v-show="!login"></v-spacer>
  </v-app-bar>
</template>

<script>
export default {
  name: "AppBar.vue",
  props:{
    login: Boolean
  }
}
</script>

<style scoped>

</style>