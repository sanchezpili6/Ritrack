<template>
  <div>
    <AppBar></AppBar>
    <div class="pets-card">
      <v-card
          v-for="pet in pets"
          :key="pet"
          class="mx-auto my-8"
          width="344"
      >
        <v-img
            src="https://lh3.googleusercontent.com/pw/AM-JKLXybhoutQ07K-2nNpFN6DEEExJRtZhGEgHv8HERkDcXzRWGcPS4TKTSEA9qKeZi547Ecyjy-RrM0EnS68RY_RVgBFk4T1_OqvfZE6FWHUhdpd8BC0Vco5XztIawAmoG6ESYEvEAkXWeE0Fk4edU4W5Apw=w1236-h927-no?authuser=0"
            height="200px"
        ></v-img>

        <v-card-title>
          {{pet.name}}
        </v-card-title>

        <v-card-actions>
          <h3 class="status mx-2">
            {{ pet.status }}
          </h3>
          <v-spacer></v-spacer>
          <v-btn color="#D46626" dark @click="editPet(pet._id)">
            Edit pet
          </v-btn>

        </v-card-actions>
      </v-card>
    </div>
    <v-btn @click="addPetModal = !addPetModal">Add Pet</v-btn>
    <v-overlay v-model="addPetModal">
      <AddPetComponent></AddPetComponent>
    </v-overlay>
    <v-overlay v-model="editPetModal">
      <EditPetComponent></EditPetComponent>
    </v-overlay>
  </div>
</template>

<script>
import AppBar from "@/components/AppBar";
import AddPetComponent from "@/components/AddPetComponent";
import EditPetComponent from "@/components/EditPetComponent";
import {get_user} from "@/helpers/Services";
import {get_pet} from "@/helpers/Services";
export default {
  name: "MyPetsView.vue",
  components:{
    AppBar,
    AddPetComponent,
    EditPetComponent
  },
  mounted() {
    if(localStorage.email){
      this.email = localStorage.email
    }
    this.getUser()
  },
  data(){
    return{
      email: '',
      user: {},
      pets:[],
      addPetModal: false,
      editPetModal: false,
      petToEdit: ''
    }
  },
  methods:{
    async getUser(){
      this.user = await get_user(this.email)
      this.pets = await this.getPet()
      console.log(this.pets)
    },
    async getPet(){
      let pets_arr = []
      for(let pet = 0; pet < this.user['pets'].length ; pet ++){
        pet = await get_pet(this.user['pets'][pet])
        pets_arr.push(pet)
      }
      return pets_arr
    },
    editPet(id){
      this.petToEdit = id
      this.editPetModal = true
    }
  }
}
</script>

<style scoped>
  .pets-card{
    display: flex;
    justify-content: space-evenly;
    align-content: space-evenly;
    margin: 50px;
    flex-wrap: wrap;
  }
  .status{
    color: #D46626;
  }
</style>
