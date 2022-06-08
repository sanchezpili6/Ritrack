<template>
  <div>
    <AppBar login></AppBar>
    <div>
      <v-row>
        <v-spacer></v-spacer>
        <img height="400" alt="Vue logo" src="../assets/ritrack.png">
        <v-spacer></v-spacer>
      </v-row>
      <div class="cards">
        <v-card
              v-for="card in cards" :key="card"
              class="mx-auto"
              max-width="344"
          >
            <v-img
                :src="card.img"
                height="200px"
            ></v-img>

            <v-card-title>
              {{card.title}}
            </v-card-title>

            <v-card-subtitle>
              {{card.subtitle}}
            </v-card-subtitle>

            <v-card-actions>
              <v-btn
                  color="orange lighten-2"
                  text
              >
                Learn more
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
                  {{card.text}}
                </v-card-text>
              </div>
            </v-expand-transition>
          </v-card>
      </div>
    </div>
  </div>
</template>

<script>
import AppBar from "@/components/AppBar";
export default {
  name: 'HomeView',
  components: {
    AppBar
  },
  data:()=>{
    return{
      show: false,
      cards:[
        {
          img:'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg',
          title: 'Top western road trips',
          subtitle:'1,000 miles of wonder',
          text: 'I\'m a thing. But, like most politicians, he promised more than he could deliver. You won\'t have time for sleeping, soldier, not with all the bed making you\'ll be doing. Then we\'ll go with that data file! Hey, you add a one and two zeros to that or we walk! You\'re going to do his laundry? I\'ve got to find a way to escape.'
        },
        {
          img:'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg',
          title: 'Top western road trips',
          subtitle:'1,000 miles of wonder',
          text: 'I\'m a thing. But, like most politicians, he promised more than he could deliver. You won\'t have time for sleeping, soldier, not with all the bed making you\'ll be doing. Then we\'ll go with that data file! Hey, you add a one and two zeros to that or we walk! You\'re going to do his laundry? I\'ve got to find a way to escape.'
        },
        {
          img:'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg',
          title: 'Top western road trips',
          subtitle:'1,000 miles of wonder',
          text: 'I\'m a thing. But, like most politicians, he promised more than he could deliver. You won\'t have time for sleeping, soldier, not with all the bed making you\'ll be doing. Then we\'ll go with that data file! Hey, you add a one and two zeros to that or we walk! You\'re going to do his laundry? I\'ve got to find a way to escape.'
        },
      ]
    }
  }
}
</script>

<style>
  .cards{
    display: flex;
    justify-content: space-evenly;
  }
</style>
