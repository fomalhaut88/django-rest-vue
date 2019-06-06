<template>
  <div v-if="persons && countries">
    <input type="button" value="New" @click="personCreate = {}">

    <div v-if="personCreate">
      <input type="text" v-model="personCreate.first_name">
      <input type="text" v-model="personCreate.last_name">
      <input type="number" v-model="personCreate.age">
      <input type="button" value="Create" :disabled="!isFull(personCreate)" @click="createPerson()">
      <input type="button" value="Hide" @click="personCreate = null">
    </div>

    <hr>

    <table>
      <tr v-for="person in persons">
        <td>{{ person.id }}</td>
        <td>{{ person.full_name }}</td>
        <td>{{ person.age }}</td>
        <td>{{ person.country ? person.country.name : '-' }}</td>
        <td><a href="#" @click="personEdit = person">edit</a></td>
      </tr>
    </table>

    <hr>

    <div v-if="personEdit">
      <input type="text" v-model="personEdit.first_name">
      <input type="text" v-model="personEdit.last_name">
      <input type="number" v-model="personEdit.age">
      <input type="password" v-model="personEdit.secret">
      <select v-model="personEdit.country">
        <option v-for="country in countries" :value="country">{{ country.name }}</option>
      </select>
      <input type="button" value="Update" :disabled="!isFull(personEdit)" @click="updatePerson()">
      <input type="button" value="Delete" @click="deletePerson()">
      <input type="button" value="Hide" @click="personEdit = null">
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        resource: this.$resource('persons{/id}/'),
        persons: null,
        personCreate: null,
        personEdit: null,
        countries: null,
      }
    },
    methods: {
      isFull(person) {
        return person.first_name && person.age
      },

      createPerson() {
        var self = this

        this.resource.save(this.personCreate).then(function(data) {
          self.persons.push(data.body)
          self.personCreate = null
        })
      },

      updatePerson() {
        var self = this

        this.resource.update({id: this.personEdit.id}, this.personEdit).then(function(data) {
          for (let i in self.persons) {
            if (self.persons[i].id == self.personEdit.id) {
              self.persons[i] = data.body
              self.personEdit = null
              break
            }
          }
        })
      },

      deletePerson() {
        var self = this

        this.resource.delete({id: this.personEdit.id}).then(function() {
          for (let i in self.persons) {
            if (self.persons[i].id == self.personEdit.id) {
              self.personEdit = null
              self.persons.splice(i, 1)
              break
            }
          }
        })
      },
    },
    mounted() {
      this.resource.get().then(data => this.persons = data.body)

      var resourceCountries = this.$resource('countries{/id}/')
      resourceCountries.get().then(data => this.countries = data.body)
    },
  }
</script>
