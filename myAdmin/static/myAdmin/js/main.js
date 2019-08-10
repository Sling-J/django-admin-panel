document.addEventListener('DOMContentLoaded', () => {
   const usersTable = document.getElementById('users-table');
   const skipUserBox = document.getElementById('skip-user-box');
   const settingsBox = document.getElementById('settings-box');

   selectHandle(usersTable);
   chooseUser(skipUserBox);
   settingsValidate(settingsBox);
});

function settingsValidate(container) {
   if (container) {
      const settingsInput = container.querySelectorAll('.settings-box__input');
      const settingsBtn = container.querySelector('.setting-box__submit button');
      const reg = /[^0-9.]/;

      const matchPhone = event => {
         if (event.target.value.search(reg) !== -1) {
            event.target.value = event.target.value.replace(reg, '');
         }
      };

      const formValidation = () => {
         let filled = true;
         let valid = false;

         settingsInput.forEach(item => {
            if (item.value.length === 0) filled = false;
         })
         
         if (
            (settingsInput[0].value > 1 || settingsInput[0].value < 0) || 
            (settingsInput[1].value > 1 || settingsInput[1].value < 0) ||
            (settingsInput[2].value < 1) || (settingsInput[3].value < 1)
         ) {
            console.log('err')
         }

         filled && valid ?
            settingsBtn.disabled = false :
            settingsBtn.disabled = true;
      };

      settingsInput.forEach(item => {
         item.addEventListener('input', matchPhone);
         item.addEventListener('change', formValidation);
      })
   }

   return;
}

function chooseUser(container) {
   if (container) {
      const skipUserRow = container.querySelectorAll('.skip-user__row');
      const skipUserBtn = container.querySelector('.skip-user__field .default-btn');
      const skipUserInput = container.querySelectorAll('.skip-user__field .skip-user__choose-field');

      skipUserRow.forEach(item => {
         const userName = item.querySelector('.skip-user-table__username span');

         item.addEventListener('click', () => {
            skipUserInput.forEach(item => {
               item.value = userName.textContent;
               item.value.length !== 0 ?
                     skipUserBtn.disabled = false :
                     skipUserBtn.disabled = true
            })
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