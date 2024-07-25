<template>
    <div class="w-max m-auto">
      <button @click="open = true">
      <div class="grid w-max"><!-- grid-rows-2 -->
          <div class="w-16 h-16 sm:w-20 sm:h-20 bg-cover m-auto" :class="team_path" :id="player.position">
            <svg v-if="player.is_captain" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" focusable="false" class="text-white"><title>Captain</title><circle cx="12" cy="12" r="12" aria-hidden="true"></circle><path d="M15.0769667,14.370341 C14.4472145,15.2780796 13.4066319,15.8124328 12.3019667,15.795341 C10.4380057,15.795341 8.92696674,14.284302 8.92696674,12.420341 C8.92696674,10.55638 10.4380057,9.045341 12.3019667,9.045341 C13.3988206,9.06061696 14.42546,9.58781014 15.0769667,10.470341 L17.2519667,8.295341 C15.3643505,6.02401882 12.1615491,5.35094208 9.51934028,6.67031017 C6.87713147,7.98967826 5.49079334,10.954309 6.17225952,13.8279136 C6.8537257,16.7015182 9.42367333,18.7279285 12.3769667,18.720341 C14.2708124,18.7262708 16.0646133,17.8707658 17.2519667,16.395341 L15.0769667,14.370341 Z" fill="currentColor" aria-hidden="true"></path></svg>
            <svg v-if="player.is_vice_captain" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" focusable="false" class="text-white"><title>Captain</title><circle cx="12" cy="12" r="12" aria-hidden="true"></circle><polygon points="13.5 .375 8.925 12.375 4.65 12.375 0 .375 3.15 .375 6.75 10.05 10.35 .375" transform="translate(5.25 6)" fill="currentColor" aria-hidden="true"></polygon></svg>
          </div>
          <div class="text-cente grid grid-rows-2 w-[75px] sm:w-[100px] text-xs sm:text-base">
            <div v-if="player.status == 'i'" class="text-center bg-red-500 text-white px-1"><p>{{player.web_name}}</p></div>
            <div v-else-if="player.status == 'd'" class="text-center bg-orange-500 text-white px-1"><p>{{player.web_name}}</p></div>
            <div v-else class="text-center bg-black text-white px-1"><p>{{player.web_name}}</p></div>
            <div class="text-center bg-white"><p>{{ player.total_points }}</p></div>
          </div>
      </div>
    </button>
  </div>
  <TransitionRoot as="template" :show="open">
      <Dialog class="relative z-10" @close="open = false">
        <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>
  
        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95" enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200" leave-from="opacity-100 translate-y-0 sm:scale-100" leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
              <DialogPanel class="relative transform overflow-hidden rounded-lg bg-white shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
                <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                  <div class="sm:items-start">
                    <!-- <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                      
                    </div> -->
                    <div class="mt-3 text-center sm:ml-4 sm:mt-0">
                    <button type="button" class="mt-3 absolute top-1 right-1 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto" @click="open = false" ref="cancelButtonRef">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" class="Dialog__CloseIcon-sc-5bogmv-3 ehxuGi"><polygon fill-rule="evenodd" points="16 13.56 10.441 8 16 2.44 13.56 0 8.001 5.56 2.441 0 .001 2.44 5.561 8 0 13.56 2.44 16 8.001 10.44 13.56 16"></polygon></svg>

                    </button>
                      <DialogTitle as="h3" class="text-2xl font-semibold leading-6 text-gray-900 pb-2">
                        {{ player.first_name }} {{ player.second_name }}
                      </DialogTitle>
                      <div v-for="game in player.explain_points" class="pt-5 border-t-2">
                        <div class="grid grid-cols-3 text-center justify-center w-1/2 m-auto">
                          <div class="m-auto">{{ game.team_h }}</div>
                          <div class="grid grid-cols-2 bg-black text-white p-1 text-2xl">
                            <div>{{ game.team_h_score }}</div>
                            <div>{{ game.team_a_score }}</div>
                          </div>
                          <div class="m-auto">{{ game.team_a }}</div>
                        </div>
                        <table class="m-auto mt-3">
                          <thead>
                            <tr>
                              <th>Statistics</th>
                              <th>Value</th>
                              <th>Points</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr v-for="info in game.stats">
                              <td>
                                {{ info.identifier }}
                              </td>
                              <td>
                                {{ info.value }}
                              </td>
                              <td>
                                {{ info.points }}
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
<!--                 <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                   <button type="button" class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 sm:ml-3 sm:w-auto" @click="open = false">Deactivate</button>
                  <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto" @click="open = false" ref="cancelButtonRef">Cancel</button>
                </div> -->
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
  <div v-if="false" class="bg-[url('/assets/img/team_shirts/1.png')] bg-[url('/assets/img/team_shirts/2.png')] bg-[url('/assets/img/team_shirts/3.png')] bg-[url('/assets/img/team_shirts/4.png')] bg-[url('/assets/img/team_shirts/5.png')]
                           bg-[url('/assets/img/team_shirts/6.png')] bg-[url('/assets/img/team_shirts/7.png')] bg-[url('/assets/img/team_shirts/8.png')] bg-[url('/assets/img/team_shirts/9.png')] bg-[url('/assets/img/team_shirts/10.png')]
                           bg-[url('/assets/img/team_shirts/11.png')] bg-[url('/assets/img/team_shirts/12.png')] bg-[url('/assets/img/team_shirts/13.png')] bg-[url('/assets/img/team_shirts/14.png')] bg-[url('/assets/img/team_shirts/15.png')]
                           bg-[url('/assets/img/team_shirts/16.png')] bg-[url('/assets/img/team_shirts/17.png')] bg-[url('/assets/img/team_shirts/18.png')] bg-[url('/assets/img/team_shirts/19.png')] bg-[url('/assets/img/team_shirts/20.png')]"></div>

</template>

<script setup>
const props = defineProps({
  player: {
    type: Object,
    required: true,
  },
});
const {player} = props;
const team_path = "bg-[url('/assets/img/team_shirts/" + player.team + ".png')]"
import { ref } from 'vue'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
const open = ref(false)
</script>