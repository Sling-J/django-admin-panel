document.addEventListener('DOMContentLoaded', () => {
   const usersTable = document.getElementById('users-table');
   const skipUserBox = document.getElementById('skip-user-box');

   selectHandle(usersTable);
   chooseUser(skipUserBox);
});

function chooseUser(container) {
   if (container) {
      const skipUserRow = container.querySelectorAll('.skip-user__row');
      const skipUserBtn = container.querySelector('.skip-user__field .default-btn');
      const skipUserInput = container.querySelector('.skip-user__field .skip-user__choose-field');

      skipUserRow.forEach(item => {
         const userName = item.querySelector('.skip-user-table__username span');

         item.addEventListener('click', () => {
            skipUserInput.value = userName.textContent;
            skipUserInput.value.length !== 0 ?
               skipUserBtn.disabled = false :
               skipUserBtn.disabled = true;
         })
      })
   }
}

function selectHandle(container) {
   if (container) {
      const selectAllCb = container.querySelector('#select-all-cb');
      const allCheckbox = container.querySelectorAll('.users-table__checkbox');

      selectAllCb.addEventListener('click', event =>
         allCheckbox.forEach(item =>
            event.target.checked ?
            item.checked = true :
            item.checked = false
         ))
   }

   return;
}