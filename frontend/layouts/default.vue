<template>
  <v-app>
    <v-app-bar color="primary">
      <v-app-bar-title>
        <nuxt-link to="/" class="text-white text-decoration-none">
          Business Bazaar
        </nuxt-link>
      </v-app-bar-title>
      
      <v-spacer />
      
      <v-btn
        to="/proposals/create"
        prepend-icon="mdi-plus"
        variant="tonal"
      >
        Создать предложение
      </v-btn>
    </v-app-bar>

    <v-main>
      <slot />
    </v-main>

    <v-footer app>
      <span>&copy; {{ new Date().getFullYear() }} Business Bazaar</span>
    </v-footer>
  </v-app>
</template> 