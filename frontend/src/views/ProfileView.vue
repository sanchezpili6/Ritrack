<template>
  <div>
    <AppBar></AppBar>
    <v-row justify="space-around" class="my-8">
      <v-card>
        <v-img
            height="250px"
            src="https://cdn.pixabay.com/photo/2020/07/12/07/47/bee-5396362_1280.jpg"
        >
          <v-card-title class="white--text mt-8 flex">
            <v-avatar size="100">
              <img
                  alt="user"
                  src="https://cdn.pixabay.com/photo/2020/06/24/19/12/cabbage-5337431_1280.jpg"
              >
            </v-avatar>
            <p class="ml-3">
              {{user.name}}
            </p>
          </v-card-title>
          <v-card-actions class="buttons">
            <v-btn x-large :href="mailto">Send email<v-icon right>mdi-email-fast</v-icon></v-btn>
          </v-card-actions>
        </v-img>
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
              <v-btn
                  color="orange lighten-2"
                  text
              >
                {{ pet.status }}
              </v-btn>

              <v-spacer></v-spacer>

              <v-btn
                  icon
                  @click="show = !show"
              >
                <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
              </v-btn>
            </v-card-actions>

            <v-expand-transition>
              <div v-show="show">
                <v-divider></v-divider>

                <v-card-text>
                  {{pet.description}}
                </v-card-text>
              </div>
            </v-expand-transition>
          </v-card>
        </div>
      </v-card>
    </v-row>
  </div>
</template>

<script>
import AppBar from "@/components/AppBar";
import {get_user} from "@/helpers/Services";
export default {
  name: "ProfileView.vue",
  components:{
    AppBar
  },
  mounted() {
    if(localStorage.email){
      this.email = localStorage.email
    }
    this.getUser()
    console.log(this.mailto)
  },
  data(){
    return{
      mailto: `mailto:${localStorage.email}?Subject=I%20may%20have%20found%20your%20pet`,
      email: '',
      user: {},
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
      show: false,
    }
  },
  methods:{
    async getUser(){
      this.user = await get_user(this.email)
      console.log(this.user)
    }
  }
}
</script>

<style scoped>
  .buttons{
    display: flex;
    justify-content: space-evenly;
  }

  .pets-card{
    display: flex;
    justify-content: space-evenly;
    align-content: space-evenly;
    margin: 50px;
    flex-wrap: wrap;
  }
</style>
