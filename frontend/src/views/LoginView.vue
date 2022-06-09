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
          <v-text-field label="User Name" outlined dense></v-text-field>
          <v-text-field label="Password" outlined dense></v-text-field>
        </v-card-text>
        <v-card-actions class="options">
          <v-btn color="#D46626" to="/signup">I don't have an account</v-btn>
          <div></div>
          <v-btn color="#FFA625" to="/lost">Continue</v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </div>
</template>

<script>
import AppBar from "@/components/AppBar";
export default {
  name: "LoginView.vue",
  components:{
    AppBar
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