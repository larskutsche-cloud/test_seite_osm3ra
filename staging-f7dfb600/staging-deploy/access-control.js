// Staging Access Control — osmera.de
// This script enforces token-based access for staging/preview deployments.
// It runs in the browser and checks for a valid access token in the URL query string.
// If no valid token is found, the page redirects to a holding page and blocks rendering.

(function() {
  'use strict';

  // Configuration — set your expected token pattern here
  // Each staging deployment generates a unique token via GitHub Actions
  const EXPECTED_TOKEN_PATTERN = /^[a-f0-9]{16}$/;

  // Optional: Whitelisted domains that can bypass token check (e.g., for testing)
  const WHITELISTED_DOMAINS = ['localhost', '127.0.0.1'];

  // DOM elements
  const body = document.body;
  const originalBodyClass = body.getAttribute('data-original-class') || '';

  // Check if we're on a staging URL (path contains /staging-)
  const isStagingUrl = window.location.pathname.includes('/staging-');

  // Check for valid token in query string
  const urlParams = new URLSearchParams(window.location.search);
  const providedToken = urlParams.get('token');

  function isValidToken(token) {
    return EXPECTED_TOKEN_PATTERN.test(token);
  }

  function isWhitelisted() {
    return WHITELISTED_DOMAINS.includes(window.location.hostname);
  }

  function createHoldingPage() {
    // Create a minimal holding page that blocks content rendering
    const holdingDiv = document.createElement('div');
    holdingDiv.style = `
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: #0a0a2e;
      color: #e0e7ff;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 999999;
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
    `;

    holdingDiv.innerHTML = `
      <div style="text-align: center; max-width: 90%; padding: 2rem;">
        <h1 style="color: #f472b6; margin-bottom: 1rem; font-size: 2.5rem;">
          🔒 Staging Environment
        </h1>
        <p style="color: #9ca3af; margin-bottom: 2rem; font-size: 1.1rem;">
          This is a preview/deployment in progress. Access is restricted.
        </p>
        <p style="color: #6b7280; margin-bottom: 2rem; font-size: 1rem;">
          If you have an access token, please append it to the URL:
        </p>
        <div style="background: #1e293b; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0;">
          <code style="color: #a78bfa; font-family: 'Fira Code', 'Consolas', monospace; user-select: none; -webkit-user-select: none;">
            ?token=YOUR_TOKEN_HERE
          </code>
        </div>
        <p style="color: #6b7280; font-size: 0.9rem; margin-top: 2rem;">
          This environment will be replaced by the final production site.
        </p>
      </div>
    `;

    // Add overlay that prevents interaction with underlying content
    const overlay = document.createElement('div');
    overlay.style = `
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.8);
      z-index: 999998;
      pointer-events: all;
    `;
    document.body.appendChild(overlay);

    // Replace body content with holding page
    body.innerHTML = '';
    body.appendChild(holdingDiv);
    body.setAttribute('data-original-class', originalBodyClass);
    body.style.position = 'fixed';
    body.style.width = '100%';
    body.style.height = '100%';
  }

  function allowContent() {
    // Remove the holding overlay and restore content
    const overlay = document.querySelector('div[style*="rgba(0,0,0,0.8)"]');
    if (overlay) {
      overlay.remove();
    }

    // Restore original body styles if we saved them
    const originalClass = body.getAttribute('data-original-class');
    if (originalClass) {
      body.setAttribute('class', originalClass);
    }
  }

  // Main access control logic
  function checkAccess() {
    // If not a staging URL, allow normal access
    if (!isStagingUrl) {
      // Remove any previously injected holding page styles/attributes
      body.removeAttribute('data-original-class');
      body.style.cssText = '';
      return;
    }

    // If on whitelisted domain (localhost, etc.), allow access
    if (isWhitelisted()) {
      allowContent();
      return;
    }

    // Check for valid token
    if (providedToken && isValidToken(providedToken)) {
      allowContent();
      return;
    }

    // No valid token found — show holding page
    createHoldingPage();
  }

  // Run on load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', checkAccess);
  } else {
    checkAccess();
  }

  // Also check on popstate/history navigation
  window.addEventListener('popstate', checkAccess);
  window.addEventListener('hashchange', checkAccess);
})();