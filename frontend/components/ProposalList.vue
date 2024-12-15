<template>
  <v-container>
    <v-row>
      <v-col
        v-for="proposal in proposals"
        :key="proposal.id"
        cols="12"
        sm="6"
        md="4"
      >
        <ProposalCard :proposal="proposal" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
const { data: proposals } = await useApi('/proposals')
</script> 