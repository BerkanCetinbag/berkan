document.addEventListener('DOMContentLoaded', function() {
    // Create modal elements
    const modal = document.createElement('div');
    modal.id = 'imageModal';
    modal.style.display = 'none';
    modal.style.position = 'fixed';
    modal.style.zIndex = '1000';
    modal.style.left = '0';
    modal.style.top = '0';
    modal.style.width = '100%';
    modal.style.height = '100%';
    modal.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
    modal.style.justifyContent = 'center';
    modal.style.alignItems = 'center';
    modal.style.overflow = 'auto';
    modal.style.paddingTop = '20px'; /* Prevent overlay on header */

    const modalContent = document.createElement('div');
    modalContent.style.position = 'relative';
    modalContent.style.margin = 'auto';
    modalContent.style.backgroundColor = '#EAE9E7';
    modalContent.style.padding = '24px';
    modalContent.style.borderRadius = '8px';
    modalContent.style.textAlign = 'center';
    modalContent.style.maxWidth = '90%'; /* Full width with margins on mobile */
    modalContent.style.boxSizing = 'border-box';

    const modalImage = document.createElement('img');
    modalImage.style.maxWidth = '100%';
    modalImage.style.height = 'auto';

    const modalText = document.createElement('p');
    modalText.style.color = '#555968';

    modalContent.appendChild(modalImage);
    modalContent.appendChild(modalText);
    modal.appendChild(modalContent);
    document.body.appendChild(modal);

    // Function to open the modal
    function openModal(imageSrc, imageAlt) {
        modalImage.src = imageSrc;
        modalImage.alt = imageAlt;
        modalText.textContent = imageAlt;
        modal.style.display = 'flex';
    }

    // Function to close the modal
    function closeModal() {
        modal.style.display = 'none';
    }

    // Add event listeners to all portfolio images
    document.querySelectorAll('.portfolio-item img').forEach(img => {
        img.addEventListener('click', function() {
            openModal(this.src, this.alt);
        });
    });

    // Close the modal when clicking outside the modal content
    modal.addEventListener('click', function(event) {
        if (event.target === modal) {
            closeModal();
        }
    });
});