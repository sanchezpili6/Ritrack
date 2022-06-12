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
            :src="pet.img"
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
          <v-btn color="#D46626" dark @click="editPetModal = !editPetModal">
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
export default {
  name: "MyPetsView.vue",
  components:{
    AppBar,
    AddPetComponent,
    EditPetComponent
  },
  data(){
    return{
      pets:[
        {
          'img':'https://www.lifespan.org/sites/default/files/styles/featured_image_large/public/lifespan-files/images/blog-images/health-beneiftis-of-pets-900x600.jpg?h=b69e0e0e&itok=PFpteD0N',
          'name': 'Firulais',
          'status': 'At home',
          'description':"I'm a good boy"
        },
        {
          'img':'https://www.lifespan.org/sites/default/files/styles/featured_image_large/public/lifespan-files/images/blog-images/health-beneiftis-of-pets-900x600.jpg?h=b69e0e0e&itok=PFpteD0N',
          'name': 'Firulais',
          'status': 'At home',
          'description':"I'm a good boy"
        },
        {
          'img':'https://www.lifespan.org/sites/default/files/styles/featured_image_large/public/lifespan-files/images/blog-images/health-beneiftis-of-pets-900x600.jpg?h=b69e0e0e&itok=PFpteD0N',
          'name': 'Firulais',
          'status': 'At home',
          'description':"I'm a good boy"
        },
      ],
      addPetModal: false,
      editPetModal: false,
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