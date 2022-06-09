<template>
  <div>
    <AppBar></AppBar>
      <v-container id="filters">
        <v-text-field label="Pet name" v-model="petName" outlined></v-text-field>
        <v-combobox
            v-model="characteristics"
            chips
            clearable
            label="Your pet's characteristics"
            multiple
            solo
            outlined
        >
          <template v-slot:selection="{ attrs, item, select, selected }">
            <v-chip
                v-bind="attrs"
                :input-value="selected"
                close
                @click="select"
                @click:close="remove(item)"
            >
              <strong>{{ item }}</strong>&nbsp;
            </v-chip>
          </template>
        </v-combobox>
        <v-btn color="#FFA625"><v-icon>mdi-magnify</v-icon>Look for pet</v-btn>
      </v-container>
      <v-row class="mx-2">
      <v-col
          v-for="n in 9"
          :key="n"
          cols="4"
          class="d-flex child-flex"
      >
        <v-card>
          <v-img
              :src="`https://picsum.photos/500/300?image=${n * 5 + 10}`"
              :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
              aspect-ratio="1"
              class="grey lighten-2"
          >
            <template v-slot:placeholder>
              <v-row
                  class="fill-height ma-0"
                  align="center"
                  justify="center"
              >
                <v-progress-circular
                    indeterminate
                    color="grey lighten-5"
                ></v-progress-circular>
              </v-row>
            </template>
          </v-img>
          <v-card-text>
            <v-chip-group
                column
            >
              <v-chip v-for="chip in chips" :key="chip">{{chip}}</v-chip>
            </v-chip-group>
          </v-card-text>

          <v-card-actions>
            <v-btn
                color="#D46626"
                text
                @click="reserve"
            >
              See pet
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import AppBar from "@/components/AppBar";
export default {
  name: "Lost&FoundView.vue",
  components:{
    AppBar
  },
  data:()=>({
    petName: '',
    characteristics: [],
    chips:['dog', 'brown', 'good boy']
  }),
  methods: {
    remove (item) {
      this.characteristics.splice(this.characteristics.indexOf(item), 1)
      this.characteristics = [...this.characteristics]
    },
  },
}
</script>

<style scoped>
</style>