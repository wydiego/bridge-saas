import type { AppProps } from 'next/app'
import Head from 'next/head'

export default function App({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <script src="https://cdn.tailwindcss.com"></script>
        <script dangerouslySetInnerHTML={{
          __html: `
            tailwind.config = {
              theme: {
                extend: {
                  colors: {
                    'bridge-blue': '#2B3A67',
                    'bridge-blue-light': '#2F5EAB',
                    'bridge-gray': '#2C2F3A',
                  }
                }
              }
            }
          `
        }} />
      </Head>
      <Component {...pageProps} />
    </>
  )
}
