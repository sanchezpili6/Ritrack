<template>
  <v-card light width="400px">
    <v-card-title class="justify-center">Edit Pet</v-card-title>
    <v-card-text>
      <v-text-field
          label="Pet name"
          outlined
          dense
          v-model="petName"
      ></v-text-field>
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
      <v-select
          v-model="status"
          :items="statuses"
          label="Your pet status"
          outlined
          dense
      ></v-select>
    </v-card-text>
    <v-card-actions class="justify-center align-content-space-around">
      <v-btn
          color="#D46626"
          text
          @click="save"
      >
        Save
      </v-btn>
      <v-btn
          color="#D46626"
          text
          @click="cancel"
      >
        Cancel
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "EditPetComponent.vue",
  data:()=>({
    petName: '',
    characteristics: [],
    chips:['dog', 'brown', 'good boy'],
    status: '',
    statuses: ['Lost', 'At home']
  }),
  methods: {
    remove (item) {
      this.characteristics.splice(this.characteristics.indexOf(item), 1)
      this.characteristics = [...this.characteristics]
    },
    save(){

    },
    cancel(){

    }
  },
}
</script>

<style scoped>

</style>