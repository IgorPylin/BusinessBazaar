<template>
  <v-card class="mx-auto my-3" max-width="400">
    <v-card-title class="text-h6">
      {{ proposal.title }}
    </v-card-title>

    <v-card-subtitle>
      {{ proposal.industry }} | {{ proposal.location }}
    </v-card-subtitle>

    <v-card-text>
      <div class="text-truncate">{{ proposal.description }}</div>
      
      <v-row class="mt-3">
        <v-col cols="6">
          <div class="text-caption">Цена</div>
          <div class="text-h6">${{ formatNumber(proposal.price) }}</div>
        </v-col>
        <v-col cols="6">
          <div class="text-caption">Годовая выручка</div>
          <div class="text-h6">${{ formatNumber(proposal.revenue) }}</div>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="6">
          <div class="text-caption">Прибыль</div>
          <div class="text-h6">${{ formatNumber(proposal.profit) }}</div>
        </v-col>
        <v-col cols="6">
          <div class="text-caption">Сотрудников</div>
          <div class="text-h6">{{ proposal.employees_count }}</div>
        </v-col>
      </v-row>
    </v-card-text>

    <v-card-actions>
      <v-btn
        variant="text"
        color="primary"
        :to="`/proposals/${proposal.id}`"
      >
        Подробнее
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup lang="ts">
interface Proposal {
  id: number
  title: string
  description: string
  price: number
  industry: string
  revenue: number
  profit: number
  employees_count: number
  location: string
}

const props = defineProps<{
  proposal: Proposal
}>()

const formatNumber = (num: number) => {
  return new Intl.NumberFormat('ru-RU').format(num)
}
</script> 