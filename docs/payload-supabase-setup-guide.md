# How to Set Up Payload with Supabase for Your Next.js App

> **Source**: [payloadcms.com](https://payloadcms.com/posts/guides/setting-up-payload-with-supabase-for-your-nextjs-app-a-step-by-step-guide)
> **Author**: Sandro Wegmann, 10xMedia
> **Date**: June 5, 2024
> **Type**: Community Guide
> **Video**: [YouTube - How to set up Payload with Supabase](https://www.youtube.com/watch?v=L5w2QYB9-UU)

---

In this post, we're going to walk you through how to set up Payload in combination with [Supabase](https://supabase.com/). This guide will walk you through the steps to integrate these two powerful tools seamlessly.

## Why Use Supabase with Payload?

Payload requires a database to function, and in most cases, you'll also need a place to store your files. While Payload can store files on your local drive, this setup is not convenient for deployments, especially in serverless environments.

[Supabase](https://supabase.com/) offers both a PostgreSQL database and multiple S3 storage buckets, making it an excellent choice for your project. Plus, Supabase's free plan provides a 500MB PostgreSQL database and 1GB of S3 storage, which should be sufficient for most small projects.

## Getting Started

1. **Open your terminal** and navigate to the folder where you want to create your project.

2. **Run the following command:**

   ```bash
   npx create-payload-app@beta
   ```

3. **Name your project:** You will be prompted to give your project a name. For this example, we'll use `supabase-payload`.

4. **Choose a project template:** Select the `blank` template since we're not building a plugin.

5. **Select a database:** Choose `PostgreSQL`. For now, use a local connection string, which we'll replace later.

## Setting Up Supabase

1. **Sign up or log in** to Supabase at [supabase.com](https://supabase.com/).

2. **Create a new project:** Name it `supabase-payload`, set a database password (you can generate one automatically), and choose your region (e.g., Frankfurt).

3. **Obtain your connection string:** Once the project setup is complete, click on `Connect` in the upper right corner to get your PostgreSQL connection string. Copy this string — you will use it to replace the local connection string in your environment variables at the next stage.

## Configuring Payload

1. **Navigate to your local project:** `cd supabase-payload`. And then open with VS Code: `code .`

2. **Update your environment variables (`.env`):** Replace the local connection string with the Supabase connection string and set your database password.

3. **Start the development server:**

   ```bash
   npm run dev
   ```

   Open `http://localhost:3000` in your browser. If you see a 404 page upon opening the URL, it's normal because we haven't created an index page yet.

   Access the admin panel at: `http://localhost:3000/admin`.

4. **Create your first user:** Follow the prompts to set up your admin user.

## Adding Users and Collections

1. **Create users:** Add a test user and verify that the users are saved in your Supabase database.

2. **Create a collection:** For demonstration, we'll create a `documents` collection:

   ```typescript
   export const documents = {
     slug: 'documents',
     fields: [
       {
         name: 'name',
         type: 'text',
         label: 'Name',
         required: true,
       },
     ],
   };
   ```

3. **Ensure the configuration in `payload.config.js`:** Add the following line to include your collection.

   ```typescript
   import path from 'path';
   import { fileURLToPath } from 'url';

   import { payloadCloudPlugin } from '@payloadcms/payload-cloud';
   import { postgresAdapter } from '@payloadcms/db-postgres'; // Updated to Postgres adapter
   import { lexicalEditor } from '@payloadcms/richtext-lexical'; // Using Lexical editor
   import { buildConfig } from 'payload/config';

   import Users from './collections/Users';
   import Documents from './collections/Documents'; // Importing Documents collection

   const filename = fileURLToPath(import.meta.url);
   const dirname = path.dirname(filename);

   export default buildConfig({
     admin: {
       user: Users.slug,
     },
     collections: [Users, Documents],
     editor: lexicalEditor({}),
     plugins: [payloadCloudPlugin()],
     secret: process.env.PAYLOAD_SECRET || '',
     typescript: {
       outputFile: path.resolve(dirname, 'payload-types.ts'),
     },
     db: postgresAdapter({
       pool: {
         connectionString: process.env.DATABASE_URI || '',
       },
     }),
   });
   ```

4. **Adjust `tsconfig.json` if using JavaScript:** If you're using JavaScript, you'll need to include JS files in your TypeScript configuration.

   ```json
   {
     "compilerOptions": {
       "paths": {},
       "target": "ES2017"
     },
     "include": [
       "next-env.d.ts",
       "**/*.ts",
       "**/*.tsx",
       ".next/types/**/*.ts",
       "**/*.js",   // If you're using JS, adjust your tsconfig file to also include JS files.
       "**/*.jsx"   // If you're using JS, adjust your tsconfig file to also include JS files.
     ],
     "exclude": [
       "node_modules"
     ]
   }
   ```

5. **Add this to your Payload config and restart the server:** `npm run dev`

6. **Finally, verify data in Supabase** — add some documents and check your Supabase database to ensure they are saved correctly.

## Warning About Database Schema

> **Important:** If you're using a PostgreSQL database, **never use your production database in your local development environment**. Changing your schema locally can override the schema in your production database and might delete an entire table. You should either use a local database for development or create a second project in Supabase for testing purposes. This will ensure you have two separate environments and avoid accidentally modifying your production database schema.

## Setting Up S3 File Storage with Payload and Supabase

1. **Install the S3 plugin:**

   ```bash
   npm install @payloadcms/storage-s3
   ```

   Since Payload is currently in beta (version 3 at the time of writing), you might encounter issues with peer dependencies. To resolve these, you can use the `legacy-peer-deps` flag. Alternatively, you could create an `.npmrc` file consisting of `legacy-peer-deps=true`.

2. **Configure the plugin:** Add the following to your Payload config:

   ```typescript
   s3Storage({
     collections: {
       media: {
         prefix: 'media',
       },
     },
     bucket: process.env.S3_BUCKET,
     config: {
       forcePathStyle: true, // Important for using Supabase
       credentials: {
         accessKeyId: process.env.S3_ACCESS_KEY_ID,
         secretAccessKey: process.env.S3_SECRET_ACCESS_KEY,
       },
       region: process.env.S3_REGION,
       endpoint: process.env.S3_ENDPOINT,
     },
   }),
   ```

   > We're using it on a media collection, which we'll create shortly. We also need to give it a bucket name and a config with the accesskey, region, and endpoint. It's also important to **force the path styles** with Supabase.

3. **Create a media collection:**

   ```typescript
   export const media = {
     slug: 'media',
     upload: true,
     fields: [],
   };
   ```

4. **Add it to your Payload config (full example with S3):**

   ```typescript
   import path from 'path';
   import { fileURLToPath } from 'url';

   import { payloadCloudPlugin } from '@payloadcms/payload-cloud';
   import { postgresAdapter } from '@payloadcms/db-postgres'; // database-adapter-import
   import { lexicalEditor } from '@payloadcms/richtext-lexical'; // editor-import
   import { buildConfig } from 'payload/config';

   import Users from './collections/Users';
   import Documents from './collections/Documents'; // Importing Documents collection
   import Media from './collections/Media'; // Importing Media collection
   import { s3Storage } from '@payloadcms/storage-s3'; // Importing S3 storage plugin

   const filename = fileURLToPath(import.meta.url);
   const dirname = path.dirname(filename);

   export default buildConfig({
     admin: {
       user: Users.slug,
     },
     collections: [Users, Documents, Media], // Add the media collection here
     editor: lexicalEditor({}),
     plugins: [payloadCloudPlugin()],
     secret: process.env.PAYLOAD_SECRET || '',
     typescript: {
       outputFile: path.resolve(dirname, 'payload-types.ts'),
     },
     db: postgresAdapter({
       pool: {
         connectionString: process.env.DATABASE_URI || '',
       },
     }),
     plugins: [
       s3Storage({
         collections: {
           media: {
             prefix: 'media',
           },
         },
         bucket: process.env.S3_BUCKET,
         config: {
           forcePathStyle: true,
           credentials: {
             accessKeyId: process.env.S3_ACCESS_KEY_ID,
             secretAccessKey: process.env.S3_SECRET_ACCESS_KEY,
           },
           region: process.env.S3_REGION,
           endpoint: process.env.S3_ENDPOINT,
         },
       }),
     ],
   });
   ```

5. **Restart the server.**

6. **Setup a bucket in Supabase:** Create a new bucket in Supabase named `supabase-payload` and get your credentials (access key and secret access key).

7. **Obtain your Supabase credentials:**
   - Go to your Supabase project dashboard.
   - Navigate to **Storage** and create a new bucket named `supabase-payload`.
   - Set the bucket to either public or private based on your needs.
   - Navigate to **Settings** and find your endpoint, region, access key, and secret access key.

8. **Update environment variables:** Add your Supabase credentials to your environment variables (`.env`):

   ```env
   S3_BUCKET=
   S3_ACCESS_KEY_ID=
   S3_SECRET_ACCESS_KEY=
   S3_REGION=
   S3_ENDPOINT=
   ```

   Restart the server.

9. **Upload an image:** Test the setup by uploading an image through the Payload admin panel and verify the upload in your Supabase storage.

---

This should provide a clear and comprehensive guide. If you encountered any confusion in this guide, please [check out the full YouTube video](https://www.youtube.com/watch?v=L5w2QYB9-UU&t=58s). Leave us any thoughts on [Discord](https://discord.gg/payload) or in the comments of the video.

Big thanks to our friends at [10xMedia.de](https://10xmedia.de/), a Payload preferred agency, who created this tutorial.
