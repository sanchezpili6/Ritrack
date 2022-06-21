  <template>
  <div>
    <AppBar></AppBar>
    <h1>Found Pets</h1>
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
      <v-btn class="mx-5" color="#FFA625"><v-icon>mdi-magnify</v-icon>Look for pet</v-btn>
      <v-btn color="#FFA625" @click="addFoundModal = !addFoundModal"><v-icon>mdi-plus</v-icon>Add Found Pet</v-btn>
    </v-container>
    <v-row class="mx-2">
      <v-col
          v-for="pet in pets"
          :key="pet"
          cols="4"
          class="d-flex child-flex"
      >
        <v-card>
          <v-img
              src="https://lh3.googleusercontent.com/pw/AM-JKLXybhoutQ07K-2nNpFN6DEEExJRtZhGEgHv8HERkDcXzRWGcPS4TKTSEA9qKeZi547Ecyjy-RrM0EnS68RY_RVgBFk4T1_OqvfZE6FWHUhdpd8BC0Vco5XztIawAmoG6ESYEvEAkXWeE0Fk4edU4W5Apw=w1236-h927-no?authuser=0"
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
              <v-chip v-for="characteristic in characteristics" :key="characteristic">{{characteristic}}</v-chip>
            </v-chip-group>
          </v-card-text>

          <v-card-actions>
            <v-btn
                color="#D46626"
                text
                :href="mailto"
            >
              Send Email
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-overlay v-model="addFoundModal">
      <v-card light width="400px">
        <v-card-title class="justify-center">Add Found Pet</v-card-title>
        <v-card-text>
          <v-text-field
              label="Pet name"
              outlined
              dense
              v-model="foundPetName"
          ></v-text-field>
          <v-text-field
              label="Location (or last seen)"
              outlined
              dense
              v-model="location"
          ></v-text-field>
          <v-combobox
              v-model="foundPetCharacteristics"
              chips
              clearable
              label="The pet's characteristics"
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
              @click="addFoundModal=!addFoundModal"
          >
            Cancel
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-overlay>
  </div>
</template>

<script>
import AppBar from "@/components/AppBar";
import {add_found_pet} from "@/helpers/Services";
import {get_found_pets} from "@/helpers/Services";
export default {
  name: "FoundView.vue",
  components:{
    AppBar
  },
  mounted() {
    this.getFoundPets()
  },
  data:()=>({
    addFoundModal: false,
    petName: '',
    characteristics: [],
    chips:['dog', 'brown', 'good boy'],
    location: '',
    pets:[],
    foundPetName: '',
    foundPetCharacteristics: [],
    mailto: `mailto:${localStorage.email}?Subject=I%20think%20that%20is%20my%20pet`,
  }),
  methods: {
    remove (item) {
      this.characteristics.splice(this.characteristics.indexOf(item), 1)
      this.characteristics = [...this.characteristics]
    },
    async save(){
      const data = {"name": this.foundPetName, "characteristics": this.foundPetCharacteristics, "location": this.location}
      await add_found_pet(data)
    },
    async getFoundPets(){
      this.pets = await get_found_pets()
    }
  },
}
</script>

<style scoped>

</style>
